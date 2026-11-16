import re,hashlib,base64,os,shutil
src=open('canon/canon.html').read()
out='pub'; shutil.rmtree(out,ignore_errors=True); os.makedirs(out+'/img'); os.makedirs(out+'/js')
seen={}
def img(m):
    mime,b64=m.group(1),m.group(2)
    data=base64.b64decode(b64); h=hashlib.sha1(data).hexdigest()[:12]
    ext={'image/webp':'webp','image/png':'png','image/jpeg':'jpg'}[mime]
    fn=f'img/{h}.{ext}'
    if fn not in seen: open(out+'/'+fn,'wb').write(data); seen[fn]=1
    return fn
c=re.sub(r'data:(image/(?:webp|png|jpeg));base64,([A-Za-z0-9+/=]+)',img,src)
n=[0]
def js(m):
    attrs,body=m.group(1),m.group(2)
    if 'src=' in attrs or len(body)<4000 or 'type=' in attrs and 'javascript' not in attrs: return m.group(0)
    n[0]+=1; fn=f'js/p{n[0]:02d}.js'; open(out+'/'+fn,'w').write(body)
    return f'<script{attrs} charset="utf-8" src="{fn}"></script>'
c=re.sub(r'<script([^>]*)>([\s\S]*?)</script>',js,c)
open(out+'/index.html','w').write('<meta charset="utf-8">'+c)
shutil.copytree('canon/voice',out+'/voice')
print('index',len(c),'imgs',len(seen),'js',n[0])
