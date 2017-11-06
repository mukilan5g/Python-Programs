import re

s = open("sample.txt", 'r')
data = s.read()
text = re.sub(r'<!.+-->',r' ',(data))

for i in re.findall(r'<([^/][^>]*)>', text):
    if ' ' in i:
        for ht in re.findall('([a-z]+)? *([a-z-]+)="([^"]+)',i):
            print ht[0]
            print('->'+ht[1]+ ' > '+ht[2])
    else:
        print i





        
