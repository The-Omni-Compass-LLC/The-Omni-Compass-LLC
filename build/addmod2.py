import sys
# replace a module's block IN PLACE (keeps load order); with a second argument (the old file) it finds the block by the old text's first 70 characters
f=sys.argv[1]; old=sys.argv[2] if len(sys.argv)>2 else f
js=open(f).read(); key=open(old).read()[:70]; p='canon/canon.html'; s=open(p).read()
i=s.find('<script>\n'+key)
if i<0: sys.exit('not found: '+f)
j=s.find('</script>',i)+len('</script>')
s=s[:i]+'<script>\n'+js+'\n</script>'+s[j:]
open(p,'w').write(s); print('in place',f,len(s))
