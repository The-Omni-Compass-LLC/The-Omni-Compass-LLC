cd /tmp/claude-0/-home-user-the-omni-compass-llc/a3311fef-b7c9-566f-8bc0-c0aede723d40/scratchpad/canon
python3 - <<'PY'
import base64,os,json
d={f[:-4]:'data:audio/mpeg;base64,'+base64.b64encode(open('voice/'+f,'rb').read()).decode() for f in sorted(os.listdir('voice')) if f.endswith('.mp3')}
open('voicemap.js','w').write('window.KANIN_VOICE='+json.dumps(d)+';')
PY
{ printf '<!doctype html>\n<html lang="en" translate="no"><head><meta charset="utf-8"><meta name="google" content="notranslate"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="description" content="KAN-IN AI Story Builder by DD Universe Multi-Media Studios. What KAN-IN KAN-DO? Let’s find out."><script>window.KANIN_STANDALONE=true</script><script>'; cat voicemap.js; printf '</script><style>body{margin:0}img{max-width:100%%}[hidden]{display:none!important}</style></head><body>\n'; cat canon.html; printf '\n</body></html>\n'; } > kanin-app.html
ls -la kanin-app.html
