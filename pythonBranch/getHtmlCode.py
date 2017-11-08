from sys import argv
import re

script,filename=argv

##outerDict={}

class htmlTags:

    def checkFile(self):
        if ".txt" in filename or ".html" in filename:
            txt=open(filename,'r')
            data=txt.read()
            print data
            self.text=re.sub(r'<!.+-->',"",data)
            #self.splitTags()
        else:
            print "The existing file is not txt or html"    

    def splitFile(self):
        useText=self.text
        for line in useText.splitlines():
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
                        keys.append(words[0])
                        values.append(words[1])
##                        innerDict={words[0]:words[1]}
##                        outerDict.update(innerDict)                
            else:
                if "<" in line and ">" in line:
                    lists=re.findall(r'[\w]+',line)
                    if len(lists)==1:
                        tagList.append(lists)
                    elif len(lists)>1:
                        for k in range(0,len(lists)):
                            if "=" in lists[k]:
                                text=lists[k]
                                wordsTwo=text.split("=")
                                keys.append(wordsTwo[0])
                                values.append(wordsTwo[1])
##                                        innerDictTwo={wordsTwo[0]:wordsTwo[1]}
##                                        outerDict=update(innerDictTwo)
                            else:
                                tagList.append(lists[k])
                    
            
            #print tagList
    def display(self):
        prompt=int(raw_input("""Enter 1.For tags,
  2.For keys,
  3.For values,
  4.For search values of corresponding key\n"""))
        if prompt==1:
            for tag in tagList:
                print tag
            self.display()   

        elif prompt==2:
            for key in keys:
                print key
            self.display()   
        elif prompt==3:
            if len(keys)==len(values):
                for ind in range(0,len(keys)):
                    print keys[ind],"=",values[ind]
            self.display()
        elif prompt==4:
            ans=raw_input("Enter key:")
            if ans in keys:
                val=keys.index(ans)
                print keys[val],"=",values[val]
            else:
                print "Enter the correct key"
                self.display()
                    
        
##        tagList=filter(None,tagList)
##        print "tag list=",tagList 
##        print "key and value=",outerDict

obj=htmlTags()
listOne=[]
tagList=[]
keys=[]
values=[]
listOfDict=[]
obj.checkFile()
obj.splitFile()
obj.display()







