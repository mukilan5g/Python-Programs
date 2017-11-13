
import sys
import re
import copy

##script,htmlCodes=argv

##outerDict={}

class htmlTags:

    def checkFile(self,htmlCodes):
        text=""

        if ".txt" in htmlCodes or ".html" in htmlCodes:
            txt=open(htmlCodes,'r')
            datas=txt.read()
            self.text=re.sub(r'<!.+-->',"",datas)
            obj=open("htmlcodes.txt","w")
            obj.write(self.text)
            #self.text=text
            #self.splitTags()
##            print self.text
##            writeHtml=open("htmlcodes.txt","w")
##            writeHtml.write(text)
##            print "writeHtml is",writeHtml
        else:
            print "The existing file is not txt or html"
            
        return self.text
    
    def splitFile(self):
        self.groupOfTags=[]
        self.groupOfKeys=[]
        self.groupOfValues=[]
        #useText = self.text
        obj2=open("htmlcodes.txt","r")
        objT=obj2.read()
        for line in objT.splitlines():
            if " " in line:
                words=line.split(" ")
                words=filter(None, words)
                word=words[0]
                word=word[1:]
                self.groupOfTags.append(word)
                    
                        #print tagList
                for index in range(1,len(words)):
                    stringWord=words[index]
                    if "=" in stringWord:
                        wordsOfLine=stringWord.split("=")
                        self.groupOfKeys.append(wordsOfLine[0])
                        self.groupOfValues.append(wordsOfLine[1])
        ##                        innerDict={words[0]:words[1]}
        ##                        outerDict.update(innerDict)                
            else:
                if "<" in line and ">" in line:
                    wordOfLine=re.findall(r'[\w]+',line)
                    if len(wordOfLine)==1:
                        word=wordOfLine[0] 
                        self.groupOfTags.append(word)
                    elif len(wordOfLine)>1:
                        for index in range(0,len(wordOfLine)):
                            if "=" in wordOfLine[index]:
                                word=wordOfLine[index]
                                word=text.split("=")
                                self.groupOfKeys.append(word[0])
                                self.groupOfValues.append(word[1])
        ##                                        innerDictTwo={wordsTwo[0]:wordsTwo[1]}
        ##                                        outerDict=update(innerDictTwo)
                            else:
                                self.groupOfTags.append(wordOfLine[index])
        List=self.groupOfTags+self.groupOfKeys+self.groupOfValues
        return List
                 
        #print tagList
    def display(self):
        issuccess = True
        try:
            prompt=int(raw_input("""Enter 1.For tags,
  2.For keys,
  3.For values,
  4.For search values of corresponding key\n"""))
            if prompt==1:
                for tag in self.groupOfTags:
                    print tag
                self.display()   

            elif prompt==2:
                for key in self.groupOfKeys:
                    print key
                self.display()   
            elif prompt==3:
                if len(self.groupOfKeys)==len(self.groupOfValues):
                    for ind in range(0,len(self.groupOfKeys)):
                        print self.groupOfKeys[ind],"=",self.groupOfValues[ind]
                    self.display()
            elif prompt==4:
                ans=raw_input("Enter key:")
                if ans in self.groupOfKeys:
                    val=self.groupOfKeys.index(ans)
                    print self.groupOfKeys[val],"=",self.groupOfValues[val]
                    
                else:
                    print "Enter the correct key"
                    self.display()
        except Exception as exception:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
            print message
            issuccess=False  
        return issuccess

##    def main(self,htmlfile):
##        self.checkFileObj=checkFile(self,htmlfile)
##        print self.checkFileObj
##        tagList=filter(None,tagList)
##        print "tag list=",tagList 
##        print "key and value=",outerDict
if __name__=='__main__':
    obj=htmlTags()
    groupOfTagsOne=[]
    groupOfKeysOne=[]
    groupOfValuesOne=[]
    List=[]
    if len(sys.argv)>1:
        obj.checkFile(sys.argv[1])
##    if len(sys.argv)>1:
##        obj.main(sys.argv[1])
    obj.splitFile()
    print "groupOfTagsOne",groupOfTagsOne
    obj.display()

