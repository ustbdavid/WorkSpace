import sys
import os

import utils
import fileinput
from language import *

print sys.argv

#print os.listdir(sys.argv[1])

mCount = 0
mMultiFlag = False
clang = CLan()

for line in utils.lines(fileinput.input(sys.argv[1])):
    print line
    if mMultiFlag is True: 
        if clang.isMultiCommentEnd(line):
            print 'multi comment end'
            mMultiFlag = False
            continue
        else:
            print 'multiflag'
            continue
        
    if clang.isSingleComment(line):
        print 'single comment'
        continue
    
    if clang.isMultiCommentBegin(line):
        print 'multi comment begin'
        mMultiFlag = True
        continue
    
    if clang.isBlank(line):
        print 'blank'
        continue
    
    print 'count: ', mCount
    mCount = mCount + 1

print 'count: ', mCount

