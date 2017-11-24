import datetime
import sys
import re
'''
General Review Comments:
-----------------------

Please read more about object oriented programming. May help you to improvise this program better.
Read about the styling guldelines of python (pep8).
'''
class htmlTags:

    def checkFile(self,htmlCodes):
        issuccess=True
        datas=""

        if ".txt" in htmlCodes or ".html" in htmlCodes: # What if the filename is created like 'sample.txt.py'. (review comment)
            txt=open(htmlCodes,'r')
            datas=txt.read()
            self.text=datas
        else:
            print "The existing file is not txt or html"
            issuccess=False   
        return datas,issuccess
    
    def splitFile(self,datas):
        issuccess = True
        try:
            htmlText=re.sub(r'<!.+-->',"",datas)
            groupOfTags=[]
            groupOfKeys=[]
            groupOfValues=[]
            for line in htmlText.splitlines():
                if " " in line:
                    words=line.split(" ")
                    words=filter(None, words)
                    word=words[0]
                    word=word[1:]
                    groupOfTags.append(word)    
                            #print tagList
                    for index in range(1,len(words)):
                        stringWord=words[index]
                        if "=" in stringWord:
                            wordsOfLine=stringWord.split("=")
                            groupOfKeys.append(wordsOfLine[0])
                            groupOfValues.append(wordsOfLine[1])
                            
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
                                else:
                                    groupOfTags.append(wordOfLine[0])               
##            List=groupOfTags+groupOfKeys+groupOfValues
            groupOfTags=list(set(groupOfTags))
            self.groupOfTags=groupOfTags
            self.groupOfKeys=groupOfKeys
            self.groupOfValues=groupOfValues
        except Exception as exception:
            issuccess=False 
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
        return groupOfTags,groupOfKeys,groupOfValues,issuccess
                 
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
            issuccess=False 
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(exception).__name__, exception.args)
        return issuccess
        

start = datetime.datetime.now()    
if __name__=='__main__':
    if len(sys.argv)>1:
        obj=htmlTags()
        returnedValue,argOne =obj.checkFile(sys.argv[1])
        if argOne:
            returnedTags,returnedKeys,returnedValues,argFour=obj.splitFile(returnedValue)
            if argFour:
                obj.display()

finish = datetime.datetime.now()
print finish-start  
