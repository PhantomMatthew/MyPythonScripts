import urllib
import re
import sys
import string
import matplotlib.pylab
import numpy
import scipy
from numpy import *
from matplotlib.pylab import *

def getDownloadAddr(html):
    reg = '<a href="http://download.pingshu8.com/([^"].*?)"'
    pattern = re.compile(reg)
    match = pattern.search(html)
    if match:
        s = match.group(1)
        return "http://download.pingshu8.com/" + s
    else:
        print "None"
        return
    return

def filesToList(initnumber, size, bitsnum, listnum):
    listdir = "G:\Python\SampleCode\list" + str(listnum) + ".txt"
    f = open(listdir, "a")
    
    for n in range(0, size + 1):
        nplus = initnumber + n
        nplusstr = ("%10." + str(bitsnum) + "d")  % nplus
        src = "http://www.pingshu8.com/down_" + str(nplusstr).strip() + ".html"
        response = urllib.urlopen(src)
        strhtml = response.read()
        strhtml = unicode(strhtml, 'gb2312','ignore').encode('gb2312','ignore')
        print getDownloadAddr(strhtml)

        f.write(getDownloadAddr(strhtml))
        f.write('\n')
    f.close()
    print "Done"

if __name__ == '__main__':
    #filesToList(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    x = linspace(0, 4*pi, 100)
    plot(x, sin(x))

