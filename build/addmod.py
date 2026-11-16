import sys,re
f=sys.argv[1]; js=open(f).read(); p='canon/canon.html'; s=open(p).read()
key=js[:70]
i=s.find('<script>\n'+key)
if i<0: i=s.find('<script>'+key)
if i>=0:
    j=s.find('</script>',i)+len('</script>')
    s=s[:i]+s[j:]
    print('replaced old block')
s=s.rstrip('\n')+'\n<script>\n'+js+'\n</script>\n'
open(p,'w').write(s); print('canon bytes',len(s))
