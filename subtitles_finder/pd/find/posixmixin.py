### -*- coding: utf-8 -*- #############################################
#######################################################################
"""Find provide a way to treatment file hierarhies and file sequence with
some conditional return.


$Id: posixmixin.py 12910 2007-11-10 19:09:37Z cray $
"""
__author__  = "Andrey Orlov, 2004"
__license__ = "GPL"
__version__ = "$Revision: 12903 $"

def _(s) : return s

import stat,os,sys

class PosixMixIn(object) :
    def isreg(self) :
        return stat.S_ISREG(self.stat[0])

    def isdir(self) :
        return stat.S_ISDIR(self.stat[0])
            
    def unlink(self) :
        os.remove(self.path)

if __name__ == '__main__' :
    print "Lads, it's only module, don't use it as application..."
    