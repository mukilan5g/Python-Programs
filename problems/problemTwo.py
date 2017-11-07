import re
s = """<head>
<title>HTML</title>
</head>
<object type="application/x-flash" data="your-file.swf" width="0" height="0">
<!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>"""


s = open("sample.txt", 'r')
data = s.read()
text = re.sub(r'<!.+-->',"",data)

for i in re.findall(r'<([^/][^>]*)>', text):
    if ' ' in i:
        for ht in re.findall('([a-z]+)? *([a-z-]+)="([^"]+)',i):
            print ht[0]
            print('->'+ht[1]+ ' > '+ht[2])
    else:
        print i






        
