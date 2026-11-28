#!/usr/bin/env bash
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License or, for a pilot, a signed, paid pilot agreement. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
# One rented Amazon EC2 machine with one NVIDIA card, for the GPU benchmark (.github/workflows/aws-gpu.yml), the way
# scripts/lambda_gpu.py rents one on Lambda: the same harness runs on it (scripts/gpu_rented_run.sh). The founder's word of
# 14 November: the one-card runs on Amazon (one card, at 1, 10 and 100 copies); the eight-card machine not now, for its cost
# an hour. Every machine this rents carries the run's number in its tags and is found by it alone; it terminates itself at
# its deadline from its own boot script (shutdown with the behaviour "terminate"), so a GitHub outage can never leave it
# billing. The keys come from the job's environment (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY), never from a file.
#
#   aws_gpu.sh price TYPE REGION                       US dollars an hour, on demand (Amazon's price list; a known table if unread)
#   aws_gpu.sh quota TYPE REGION [ASK]                 the G and VT on-demand vCPU quota has room for TYPE (exit 0), or says
#                                                      why not (exit 2); ASK=n files an increase to n vCPUs with Amazon
#   aws_gpu.sh ami REGION                              the newest Deep Learning AMI with NVIDIA's driver and PyTorch (Ubuntu)
#   aws_gpu.sh launch TYPE REGION NAME RUN PUB HOURS   the key, the firewall (port 22 from this runner only), the machine;
#                                                      prints "instance-id security-group-id"
#   aws_gpu.sh allow SG REGION                         port 22 from this runner too (each watch job runs on its own runner)
#   aws_gpu.sh wait ID REGION                          until running; prints the public address
#   aws_gpu.sh status ID [REGION]                      prints "ID NAME STATE" (STATE terminated once it is gone)
#   aws_gpu.sh terminate [ID] --run RUN [REGION]       gives back the machine and every machine tagged with the run, then its
#                                                      key and firewall; exit 2 if Amazon does not confirm
set -uo pipefail
cmd="${1:-}"; shift || true
export AWS_PAGER=""
REGION_DEFAULT="${AWS_REGION:-us-east-1}"

price() {   # TYPE REGION
  local t="$1" r="$2" p=""
  p=$(aws pricing get-products --region us-east-1 --service-code AmazonEC2 --output json --filters \
      "Type=TERM_MATCH,Field=instanceType,Value=$t" "Type=TERM_MATCH,Field=regionCode,Value=$r" \
      "Type=TERM_MATCH,Field=operatingSystem,Value=Linux" "Type=TERM_MATCH,Field=tenancy,Value=Shared" \
      "Type=TERM_MATCH,Field=preInstalledSw,Value=NA" "Type=TERM_MATCH,Field=capacitystatus,Value=Used" 2>/dev/null \
    | python3 -c "
import json, sys
d = json.load(sys.stdin)
for item in d.get('PriceList', []):
    o = json.loads(item)
    for term in o.get('terms', {}).get('OnDemand', {}).values():
        for dim in term.get('priceDimensions', {}).values():
            v = float(dim.get('pricePerUnit', {}).get('USD', 0) or 0)
            if v > 0:
                print(v); sys.exit(0)
" 2>/dev/null)
  if [ -z "$p" ]; then   # Amazon's published on-demand prices in us-east-1, us-east-2 and us-west-2 (Linux, shared), read 14 November 2026
    case "$t" in
      g5.xlarge) p=1.006;; g5.2xlarge) p=1.212;; g5.4xlarge) p=1.624;; g6.xlarge) p=0.8048;; g6.2xlarge) p=0.9776;;
      g4dn.xlarge) p=0.526;; g4dn.2xlarge) p=0.752;;
      *) echo "no price known for $t: give its price with PRICE=<dollars an hour>" >&2; [ -n "${PRICE:-}" ] && p="$PRICE" || return 2;;
    esac
  fi
  echo "$p"
}

vcpus() { aws ec2 describe-instance-types --region "$2" --instance-types "$1" --query 'InstanceTypes[0].VCpuInfo.DefaultVCpus' --output text; }

quota() {   # TYPE REGION [ASK]
  local t="$1" r="$2" ask="${3:-}" need have open
  need=$(vcpus "$t" "$r") || { echo "quota: $t is not offered in $r"; return 2; }
  # L-DB2E81BA: Running On-Demand G and VT instances, counted in vCPUs
  have=$(aws service-quotas get-service-quota --region "$r" --service-code ec2 --quota-code L-DB2E81BA \
         --query 'Quota.Value' --output text 2>/dev/null | cut -d. -f1)
  [ -n "$have" ] && [ "$have" != None ] || have=$(aws service-quotas get-aws-default-service-quota --region "$r" \
         --service-code ec2 --quota-code L-DB2E81BA --query 'Quota.Value' --output text 2>/dev/null | cut -d. -f1)
  # the vCPUs of G and VT machines already running on the account count against the same quota
  local used
  used=$(aws ec2 describe-instances --region "$r" --filters "Name=instance-state-name,Values=pending,running" \
         --query 'Reservations[].Instances[].[InstanceType,CpuOptions.CoreCount,CpuOptions.ThreadsPerCore]' --output text 2>/dev/null \
         | awk '$1 ~ /^(g|vt)[0-9]/ {s += $2 * $3} END {print s + 0}')
  echo "quota: $t needs $need vCPUs; the G and VT quota in $r is ${have:-unread}, $used in use"
  if [ -n "$have" ] && [ "$have" != None ] && [ $(( have - used )) -ge "$need" ]; then return 0; fi
  if [ -n "$ask" ]; then
    open=$(aws service-quotas list-requested-service-quota-change-history-by-quota --region "$r" --service-code ec2 \
           --quota-code L-DB2E81BA --query "length(RequestedQuotas[?Status=='PENDING' || Status=='CASE_OPENED'])" --output text 2>/dev/null || echo 0)
    if [ "${open:-0}" != 0 ]; then
      echo "quota: an increase is already asked of Amazon and open; nothing rented until Amazon grants it"
    elif aws service-quotas request-service-quota-increase --region "$r" --service-code ec2 --quota-code L-DB2E81BA \
         --desired-value "$ask" > /dev/null 2> quota.err; then
      echo "quota: asked Amazon for $ask G and VT vCPUs in $r (Amazon answers by e-mail, often within a day); nothing rented"
    else
      echo "quota: the increase could not be asked ($(tr '\n' ' ' < quota.err | cut -c1-300)); nothing rented"
    fi
  fi
  return 2
}

ami() {   # REGION
  aws ec2 describe-images --region "$1" --owners amazon --filters \
    "Name=name,Values=Deep Learning OSS Nvidia Driver AMI GPU PyTorch * (Ubuntu 2?.04) *" "Name=state,Values=available" \
    "Name=architecture,Values=x86_64" --query 'sort_by(Images,&CreationDate)[-1].[ImageId,Name,RootDeviceName,BlockDeviceMappings[0].Ebs.VolumeSize]' --output text
}

myip() { curl -fsS --max-time 20 https://checkip.amazonaws.com | tr -d '[:space:]'; }

allow() {   # SG REGION
  local ip; ip=$(myip) || { echo "allow: this runner's address could not be read"; return 2; }
  aws ec2 authorize-security-group-ingress --region "$2" --group-id "$1" --protocol tcp --port 22 --cidr "$ip/32" > /dev/null 2>&1 || true
  echo "allow: port 22 from $ip"
}

launch() {   # TYPE REGION NAME RUN PUB HOURS
  local t="$1" r="$2" name="$3" run="$4" pub="$5" hours="$6" vpc sg img dev size mins id sub
  read -r img _ dev size < <(ami "$r" | awk -F'\t' '{print $1, "x", $3, $4}')
  [ -n "$img" ] && [ "$img" != None ] || { echo "launch: no Deep Learning AMI found in $r" >&2; return 2; }
  [ "${size:-0}" -ge 120 ] 2>/dev/null || size=120
  vpc=$(aws ec2 describe-vpcs --region "$r" --filters Name=isDefault,Values=true --query 'Vpcs[0].VpcId' --output text)
  if [ -z "$vpc" ] || [ "$vpc" = None ]; then
    vpc=$(aws ec2 create-default-vpc --region "$r" --query 'Vpc.VpcId' --output text) || { echo "launch: no default network in $r" >&2; return 2; }
  fi
  aws ec2 import-key-pair --region "$r" --key-name "omni-gh-$run" --public-key-material "fileb://$pub" \
    --tag-specifications "ResourceType=key-pair,Tags=[{Key=omni-run,Value=$run}]" > /dev/null
  sg=$(aws ec2 create-security-group --region "$r" --vpc-id "$vpc" --group-name "omni-gh-$run" \
       --description "Omni-Compass GPU run $run: ssh from the GitHub runner only" \
       --tag-specifications "ResourceType=security-group,Tags=[{Key=omni-run,Value=$run}]" --query GroupId --output text)
  allow "$sg" "$r" >&2
  mins=$(python3 -c "print(max(10, int(float('$hours') * 60)))")
  # the machine gives itself back at its deadline, whatever happens to GitHub (shutdown, behaviour terminate)
  printf '#!/bin/bash\nshutdown -h +%s "Omni-Compass run deadline"\n' "$mins" > userdata.sh
  for sub in $(aws ec2 describe-subnets --region "$r" --filters "Name=vpc-id,Values=$vpc" "Name=default-for-az,Values=true" \
               --query 'Subnets[].SubnetId' --output text); do
    id=$(aws ec2 run-instances --region "$r" --image-id "$img" --instance-type "$t" --count 1 --key-name "omni-gh-$run" \
         --security-group-ids "$sg" --subnet-id "$sub" --associate-public-ip-address \
         --instance-initiated-shutdown-behavior terminate --user-data file://userdata.sh \
         --block-device-mappings "DeviceName=$dev,Ebs={VolumeSize=$size,VolumeType=gp3,DeleteOnTermination=true}" \
         --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=$name},{Key=omni-run,Value=$run}]" \
                              "ResourceType=volume,Tags=[{Key=omni-run,Value=$run}]" \
         --query 'Instances[0].InstanceId' --output text 2> launch.err) && break
    echo "launch: not in $sub ($(tr '\n' ' ' < launch.err | cut -c1-200)); the next zone" >&2; id=""
  done
  [ -n "$id" ] || { echo "launch: no zone in $r had a $t: $(tr '\n' ' ' < launch.err | cut -c1-300)" >&2; return 2; }
  echo "$id $sg"
}

wait_up() {   # ID REGION
  aws ec2 wait instance-running --region "$2" --instance-ids "$1" || return 2
  aws ec2 describe-instances --region "$2" --instance-ids "$1" --query 'Reservations[0].Instances[0].PublicIpAddress' --output text
}

status() {   # ID [REGION]
  local r="${2:-$REGION_DEFAULT}" s n
  read -r s n < <(aws ec2 describe-instances --region "$r" --instance-ids "$1" \
    --query 'Reservations[0].Instances[0].[State.Name,Tags[?Key==`Name`]|[0].Value]' --output text 2>/dev/null)
  case "$s" in shutting-down|terminated|"") s=terminated;; esac
  echo "$1 ${n:-none} $s"
}

terminate() {   # [ID] --run RUN [REGION]
  local ids=() run="" r="$REGION_DEFAULT" bad=0
  while [ $# -gt 0 ]; do case "$1" in --run) run="$2"; shift 2;; --region) r="$2"; shift 2;; i-*) ids+=("$1"); shift;; *) shift;; esac; done
  if [ -n "$run" ]; then
    mapfile -t more < <(aws ec2 describe-instances --region "$r" --filters "Name=tag:omni-run,Values=$run" \
      "Name=instance-state-name,Values=pending,running,stopping,stopped" --query 'Reservations[].Instances[].InstanceId' --output text | tr '\t' '\n' | grep . || true)
    ids+=("${more[@]}")
  fi
  mapfile -t ids < <(printf '%s\n' "${ids[@]}" | grep . | sort -u)
  if [ "${#ids[@]}" -gt 0 ]; then
    aws ec2 terminate-instances --region "$r" --instance-ids "${ids[@]}" --query 'TerminatingInstances[].[InstanceId,CurrentState.Name]' --output text | sed 's/^/  given back: /'
    aws ec2 wait instance-terminated --region "$r" --instance-ids "${ids[@]}" || bad=1
  fi
  if [ -n "$run" ]; then
    aws ec2 delete-key-pair --region "$r" --key-name "omni-gh-$run" > /dev/null 2>&1 || true
    for sg in $(aws ec2 describe-security-groups --region "$r" --filters "Name=tag:omni-run,Values=$run" --query 'SecurityGroups[].GroupId' --output text); do
      for i in 1 2 3 4 5 6; do aws ec2 delete-security-group --region "$r" --group-id "$sg" > /dev/null 2>&1 && break; sleep 20; done
    done
  fi
  [ "$bad" = 0 ] || { echo "terminate: Amazon did not confirm every machine given back: ${ids[*]}"; return 2; }
  echo "terminate: ${#ids[@]} machine(s) given back${run:+ for run $run}"
}

case "$cmd" in
  price) price "$@";;
  quota) quota "$@";;
  ami) ami "$@";;
  launch) launch "$@";;
  allow) allow "$@";;
  wait) wait_up "$@";;
  status) status "$@";;
  terminate) terminate "$@";;
  *) echo "usage: aws_gpu.sh price|quota|ami|launch|allow|wait|status|terminate ..."; exit 2;;
esac
