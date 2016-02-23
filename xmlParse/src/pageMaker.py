from xml.sax.handler import ContentHandler
from xml.sax import parse
import os 

class PageMaker(ContentHandler):
    passthrough = False
    preDir = ''
    currentDir = os.getcwd()
    def startElement(self, name, attrs):
        if name == 'page':
            self.passthrough = True
            self.out = open(os.path.join(self.currentDir, attrs['name'] + '.html'), 'w')
            self.out.write('<html><haed>\n')
            self.out.write('<title>%s</title>' % attrs['title'])
            self.out.write('</head><body>\n')
        elif self.passthrough:
            self.out.write('<' + name)
            for key, value in attrs.items():
                self.out.write(' %s="%s"' % (key, value))
            self.out.write('>')
        
        if name == 'directory':
            self.preDir = self.currentDir
            self.currentDir = os.path.join(self.currentDir, attrs['name'])
            os.mkdir(self.currentDir)
            
    def endElement(self, name):
        if name == 'page':
            self.passthrough = False
            self.out.write('\n</body></html>\n')
            self.out.close()
        elif self.passthrough:
            self.out.write('</%s>' % name)
            
        if name == 'directory':
            self.currentDir = self.preDir
            
    def characters(self, content):
        if self.passthrough:
            self.out.write(content)
            
parse('website.xml', PageMaker())
