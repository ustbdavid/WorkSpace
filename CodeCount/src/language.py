import re

class CLan:
    def filter(self, name):
        last = name[-2:]
        return (last == '.c') or (last == '.h')
    
    def isSingleComment(self, line):
        pattern = r'(^//)|(^/\*.*\*/$)'
        return re.match(pattern, line.strip())
    
    def isMultiCommentBegin(self, line):
        return self._isMultiCommentBegin(line) and (not self._isMultiCommentEnd(line))
    
    def isMultiCommentEnd(self, line):
        return self._isMultiCommentEnd(line) and (not self._isMultiCommentBegin(line))
    
    def isBlank(self, line):
        return len(line.strip()) == 0
    
    def _isMultiCommentBegin(self, line):
        pattern = r'^/\*'
        return re.match(pattern, line.strip())
    
    def _isMultiCommentEnd(self, line):
        pattern = r'\*/[\r\n]*$'
        #print '===', line, ', ', line.strip().strip('\r').strip('\n')
        return re.search(pattern, line.strip().strip('\r').strip('\n'))
    
class PyLan:
    def filter(self, name):
        last = name[-3:]
        return last == '.py'
    
