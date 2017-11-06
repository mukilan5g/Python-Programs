import re

s = """<head>
<title>HTML</title>
</head>
<object type="application/x-flash" data="your-file.swf" width="0" height="0">
<!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>"""


match = re.finditer(r'<!--[^/!].+?-->|(?<=<)[^/!].*?(?=>)', s)
for m in match:
    n = m.group()
    if not re.match(r'<!', n):
        print re.match(r'.+?(?=\s|$)', n).group()
        for k in re.finditer(r'(?<=\s)(\S.+?)="(.+?)"', n):
            print '-> ' + k.group(1) + ' > ' + k.group(2)         

