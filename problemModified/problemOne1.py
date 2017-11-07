from sys import argv
import re
script,filename=argv
listOne=[]
tagList=[]
outerDict={}
listOfDict=[]
if ".txt" in filename or ".html" in filename:
    print "the existing file is in txt or html format"
    txt=open(filename,'r')
    data=txt.read()
    text=re.sub(r'<!.+-->',"",data)
    for line in text.splitlines():
        if " " in line:
            listOne=line.split(" ")
            #listOne.append(words)
            strOne=listOne[0]
            strOne=strOne[1:]
            tagList.append(strOne)
            #print tagList
            for lineTwo in range(1,len(listOne)):
                strTwo=listOne[lineTwo]
                if "=" in strTwo:
                    words=strTwo.split("=")
                    innerDict={words[0]:words[1]}
                    outerDict.update(innerDict)                
        else:
            line=line[1:len(line)-1]
            tagList.append(line)
            #print tagList
else:            
    print "The existing file is not txt or html"
    
print "tag list=",tagList
print "key and value=",outerDict



##output
##the existing file is in txt or html format
##tag list= ['head', 'title>HTML</title', '/head', 'object', '', '', '/object']
##key and value= {'width': '"0"', 'name': '"quality"', 'type': '"application/x-flash"', 'data': '"your-file.swf"', 'value': '"high"/>', 'height': '"0">'}

























    
