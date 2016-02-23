import unittest
from language import *
import unittest

class CLangTestCase(unittest.TestCase):
    def setUp(self):
        print 'setup'
        unittest.TestCase.setUp(self)
        self.clang = CLan()
        
    def testFilter(self):
        name = "xx.c"
        self.failUnless(self.clang.filter(name))
        
        name = "xx.h"
        self.failUnless(self.clang.filter(name))
        
        name = "xx.cpp"
        self.failIf(self.clang.filter(name))
        
        name = "xxc"
        self.failIf(self.clang.filter(name))
        
    def testCSingleComment(self):
        line = '//xxx'
        self.failUnless(self.clang.isSingleComment(line))
        
        line = 'xx//xx'
        self.failIf(self.clang.isSingleComment(line))
        
        line = 'xxx//'
        self.failIf(self.clang.isSingleComment(line))
        
        line = '/*xxx*/'
        self.failUnless(self.clang.isSingleComment(line))
        
        line = '/*//'
        self.failIf(self.clang.isSingleComment(line))
        
        line = '/*xxx'
        self.failIf(self.clang.isSingleComment(line))
        
    def testCMultiCommentBegin(self):
        line = '/*xxx'
        self.failUnless(self.clang.isMultiCommentBegin(line))
        
        line = '/*xxx*/'
        self.failIf(self.clang.isMultiCommentBegin(line))
        
        line = '//'
        self.failIf(self.clang.isMultiCommentBegin(line))
        
    def testCMultiCommentEnd(self):
        line = 'xxx*/'
        self.failUnless(self.clang.isMultiCommentEnd(line))
        
        line = 'xxx*/\n\r'
        self.failUnless(self.clang.isMultiCommentEnd(line))
        
        line = '/*xxx*/'
        self.failIf(self.clang.isMultiCommentEnd(line))
        
        line = '//'
        self.failIf(self.clang.isMultiCommentEnd(line))
        
    def testCBlank(self):
        line = '  '
        self.failUnless(self.clang.isBlank(line))
        
        line = '  x'
        self.failIf(self.clang.isBlank(line))
        
        line = '  //'
        self.failIf(self.clang.isBlank(line))
    
print __name__
if __name__ == '__main__': unittest.main()