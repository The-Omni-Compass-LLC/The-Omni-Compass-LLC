import os,json,subprocess,glob,re
OUT='pub/voice' if not os.environ.get('VOUT') else os.environ['VOUT']
os.makedirs(OUT,exist_ok=True); CH=1_000_000
def key(t):
    t=re.sub(r'\s+',' ',t).strip(); h=5381; b=t.encode('utf-16-le')
    for i in range(0,len(b),2):
        cu=b[i]|(b[i+1]<<8); h=((h*33)^cu)&0xffffffff
    s='';n=h;al='0123456789abcdefghijklmnopqrstuvwxyz'
    while True:
        s=al[n%36]+s; n//=36
        if n==0: break
    return 'g'+s
G=[key(t) for t in json.load(open('tourlines.json'))]
def order(names):
    nm=[n for n in names if not n.startswith('g')]
    rank={'x':0,'tour':1,'auto':2}
    nm.sort(key=lambda n:(rank.get(n.split('-')[0],3),[int(x) if x.isdigit() else x for x in re.split(r'(\d+)',n)]))
    gs=[g for g in G if g in names]+sorted(n for n in names if n.startswith('g') and n not in G)
    return nm+gs
SRC={'af_heart':['canon/voice','tts2/out']}
for v in ['af_bella','am_michael','bf_emma','bm_george','am_fenrir']: SRC[v]=['tts3/'+v]
vmap={}
for v,dirs in SRC.items():
    files={}
    for d in dirs:
        for p in glob.glob(d+'/*.mp3'):
            if os.path.getsize(p)>1000: files[os.path.basename(p)[:-4]]=p
    if not files: continue
    m={}; part=0; buf=bytearray()
    for name in order(list(files)):
        raw=subprocess.run(['ffmpeg','-loglevel','error','-i',files[name],'-c:a','copy','-map_metadata','-1','-id3v2_version','0','-write_xing','0','-f','mp3','-'],capture_output=True,check=True).stdout
        if buf and len(buf)+len(raw)>CH:
            open(f'{OUT}/v-{v}-{part}.mp3','wb').write(buf); part+=1; buf=bytearray()
        m[name]=[f'v-{v}-{part}.mp3',len(buf),len(raw)]; buf+=raw
    if buf: open(f'{OUT}/v-{v}-{part}.mp3','wb').write(buf); part+=1
    vmap[v]=m; print(v,len(m),'clips',part,'files')
json.dump(vmap,open(OUT+'/vmap.json','w'),separators=(',',':'))
