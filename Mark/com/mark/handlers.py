from re import match

class Handler:
    def callback(self, prefix, name, *args):
        method = getattr(self, prefix+name, None)
        if callable(method):
            return method(*args)
        
    def start(self, name):
        self.callback('start_', name)
        
    def end(self, name):
        self.callback('end_', name)
    
    #The second parameter of re.sub is a function, need to return a function here        
    def sub(self, name):
        def substitution(match):
            result = self.callback('sub_', name, match)
            if result is None: result = match.group(0)
            return result
        
        return substitution
    
    
class HTMLRender(Handler):
    def start_document(self):
        print '<html><head><title>...</title></head><body>'
        
    def end_document(self):
        print '</body></html>'
    
    def start_heading(self):
        print '<h2>'
        
    def end_heading(self):
        print '</h2>'
        
    def start_title(self):
        print '<hl>'
        
    def end_title(self):
        print '</hl>'    
    
    def start_paragraph(self):
        print '<p>'
        
    def end_paragraph(self):
        print '</p>'
        
    def sub_emphasis(self, match):
        return '<em>%s</em>' % match.group(1)
    
    def feed(self, data):
        print data