from unittest import TestCase
from getHtmlCode import htmlTags

class TestHtmlTags(TestCase):
    
    textFile=open("htmlFile.txt","r")
    txtFile=textFile.read()
    def test(self):
        
        self.assertEqual(txtFile,h.checkFile())
        
if __name__ == '__main__':
    unittest.main()
