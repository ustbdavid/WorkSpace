from xml.sax.handler import ContentHandler
from xml.sax import parse

class HeadinglineHandler(ContentHandler):
    
    in_headline = False
    def __init__(self, headlines):
        ContentHandler.__init__(self)
        self.headlines = headlines
        self.data = []
        
    def startElement(self, name, attrs):
#         print name
        if name == 'h1':
            self.in_headline = True
            
    def endElement(self, name):
        if name == 'h1':
            text = ''.join(self.data)
            self.data = []
            self.headlines.append(text)
            self.in_headline = False
            
    def characters(self, content):
        if self.in_headline:
            print 'meet char ', content
            self.data.append(content)
            
headlines = []
parse('website.xml', HeadinglineHandler(headlines))

print headlines