import sys, re
from util import blocks

print '<html><head><title>...</title><body>'

title = True

for block in blocks(sys.stdin):
    #print block
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
    if title:
        print '<hl>'
        print block
        print '</hl>'
        title = False
    else:
        print '<p>'
        print block
        print '</p>'
        
print '</body></head></html>'