from sys import argv
script,inputFile=argv
def printAll(currentFile):
    print currentFile.read()
def printSpecific(currentFile):
    print currentFile.seek(0)
def printALine(lineCount,filee):
    print lineCount,filee.readline()
currentFile=open(inputFile,"rw+")

printAll(currentFile)
printSpecific(currentFile)
currentLine=1
printALine(currentLine,currentFile)
currentLine=currentLine+1
printALine(currentLine,currentFile)
