set -e
cd /tmp/claude-0/-home-user-the-omni-compass-llc/a3311fef-b7c9-566f-8bc0-c0aede723d40/scratchpad
python3 mkpub.py
node tz/strip.js pub/js/p*.js >/dev/null
python3 mkhvkeys.py pub/js/hvkeys.js
python3 - <<'PY'
p='pub/index.html'; s=open(p).read()
s=s.replace('<meta charset="utf-8">','<meta charset="utf-8"><script charset="utf-8" src="js/hvkeys.js"></script>',1)
open(p,'w').write(s)
PY
D=pub
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
cp -r samples_keep pub/samples
find pub/voice -name '*.mp3' ! -name 'v-*' -delete
python3 mkvsprite.py
for f in pub/js/p*.js; do node --check $f || echo BAD $f; done
echo BUILD_OK
