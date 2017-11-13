import unittest
from getHtmlCode import htmlTags
from getHtmlCode import  *
class TestHtmlTags(unittest.TestCase):
    def setUp(self):
        self.textFile=open("htmlFile.txt","r").read()
        self.expected=self.textFile
        expectedTags=["html","head","title","title","head","object","param","object","html"]
        expectedKeys=['type', 'data', 'width', 'height', 'name', 'value']
        expectedValues=['"application/x-flash"', '"your-file.swf"', '"0"', '"0"', '"quality"', '"high"']
        self.ListOfHtml=expectedTags+expectedKeys+expectedValues
    def testcheckFile(self):
        h=htmlTags()
        actual=h.checkFile("htmlFile.txt")
        self.assertNotEqual(actual,self.expected)

    def testsplitFile(self):
        h=htmlTags()
        actualTwo=h.splitFile()
        self.assertNotEqual(actualTwo,self.ListOfHtml)
    def testDisplay(self):
        h=htmlTags()
        check=True
        self.assertNotEqual(h.display(),check)
    
        

if __name__ == '__main__':
    unittest.main()
