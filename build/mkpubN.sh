set -e
D=$1
cd /tmp/claude-0/-home-user-the-omni-compass-llc/a3311fef-b7c9-566f-8bc0-c0aede723d40/scratchpad
sed "s/out='pub'/out='$D'/" mkpub.py > mkpub_$D.py
python3 mkpub_$D.py >/dev/null && node tz/strip.js $D/js/p*.js >/dev/null && python3 mkhvkeys.py $D/js/hvkeys.js >/dev/null
python3 - "$D" <<'PY'
import sys
D=sys.argv[1]; p=D+'/index.html'; s=open(p).read(); s=s.replace('<meta charset="utf-8">','<meta charset="utf-8"><script charset="utf-8" src="js/hvkeys.js"></script>',1); open(p,'w').write(s)
open(D+'/ptest.html','w').write('<meta name="viewport" content="width=device-width,initial-scale=1">'+s)
PY
python3 - "$D" <<'PY2'
import sys,time
D=sys.argv[1]; v=time.strftime('%Y%m%d%H%M%S',time.gmtime())
p=D+'/index.html'; s=open(p).read()
if 'window.KANIN_BUILD=' not in s: s=s.replace('<meta charset="utf-8">','<meta charset="utf-8"><script>window.KANIN_BUILD="%s"</script>'%v,1)
open(p,'w').write(s); open(D+'/version.json','w').write('{"v":"%s"}'%v)
t=D+'/ptest.html'
try:
    q=open(t).read()
    if 'window.KANIN_BUILD=' not in q: open(t,'w').write(q.replace('<meta charset="utf-8">','<meta charset="utf-8"><script>window.KANIN_BUILD="%s"</script>'%v,1))
except FileNotFoundError: pass
PY2
ln -sfn ../samples_keep $D/samples; cp pub/voice/vmap.json pub/voice/v-*.mp3 $D/voice/ 2>/dev/null || true
for f in $D/js/p*.js; do node --check $f || echo BAD $f; done; echo ${D}_OK
