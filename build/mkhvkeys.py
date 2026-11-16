import os,json,sys
out=sys.argv[1]
ks=sorted(f[:-4] for f in os.listdir('tts2/out') if f.startswith('g') and f.endswith('.mp3') and os.path.getsize('tts2/out/'+f)>1000)
open(out,'w').write('window.HVKEYS='+json.dumps({k:1 for k in ks},separators=(',',':'))+';')
print('hvkeys',len(ks))
