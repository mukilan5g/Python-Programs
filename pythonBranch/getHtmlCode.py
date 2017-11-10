
from sys import argv
import re

script,htmlCodes=argv

##outerDict={}

class htmlTags:

    def checkFile(self):
        text=""
        if ".txt" in htmlCodes or ".html" in htmlCodes:
            txt=open(htmlCodes,'r')
            datas=txt.read()
            print datas
            self.text=re.sub(r'<!.+-->',"",datas)
            #self.splitTags()
        else:
            print "The existing file is not txt or html"    
        return text
    def splitFile(self):
        useText=self.text
        for line in useText.splitlines():
            if " " in line:
                words=line.split(" ")
                words=filter(None, words)
                word=words[0]
                word=word[1:]
                groupOfTags.append(word)
                print "word is",word
            
                #print tagList
                for index in range(1,len(words)):
                    stringWord=words[index]
                    if "=" in stringWord:
                        wordsOfLine=stringWord.split("=")
                        groupOfKeys.append(wordsOfLine[0])
                        groupOfValues.append(wordsOfLine[1])
##                        innerDict={words[0]:words[1]}
##                        outerDict.update(innerDict)                
            else:
                if "<" in line and ">" in line:
                    wordOfLine=re.findall(r'[\w]+',line)
                    if len(wordOfLine)==1:
                        word=wordOfLine[0] 
                        groupOfTags.append(word)
                    elif len(wordOfLine)>1:
                        for index in range(0,len(wordOfLine)):
                            if "=" in wordOfLine[index]:
                                word=wordOfLine[index]
                                word=text.split("=")
                                groupOfKeys.append(word[0])
                                groupOfValues.append(word[1])
##                                        innerDictTwo={wordsTwo[0]:wordsTwo[1]}
##                                        outerDict=update(innerDictTwo)
                            else:
                                groupOfTags.append(wordOfLine[index])
                    
        return groupOfTags,groupOfKeys,groupOfValues
            #print tagList
    def display(self):
        issuccess = True
        try:
            prompt=int(raw_input("""Enter 1.For tags,
  2.For keys,
  3.For values,
  4.For search values of corresponding key\n"""))
            if prompt==1:
                for tag in groupOfTags:
                    print tag
                self.display()   

            elif prompt==2:
                for key in groupOfKeys:
                    print key
                self.display()   
            elif prompt==3:
                if len(groupOfKeys)==len(groupOfValues):
                    for ind in range(0,len(groupOfKeys)):
                        print groupOfKeys[ind],"=",groupOfValues[ind]
                    self.display()
            elif prompt==4:
                ans=raw_input("Enter key:")
                if ans in groupOfKeys:
                    val=groupOfKeys.index(ans)
                    print groupOfKeys[val],"=",groupOfValues[val]
                    
                else:
                    print "Enter the correct key"
                    self.display()
        except:
            issuccess=False  
        return issuccess
##        tagList=filter(None,tagList)
##        print "tag list=",tagList 
##        print "key and value=",outerDict

obj=htmlTags()
groupOfTags=[]
groupOfKeys=[]
groupOfValues=[]

obj.checkFile()
obj.splitFile()
obj.display()

