### -*- coding: utf-8 -*- #############################################
#######################################################################
"""Find provide a way to treatment file hierarhies and file sequence with
some conditional return.


$Id: find.py 12910 2007-11-10 19:09:37Z cray $
"""
__author__  = "Andrey Orlov, 2004"
__license__ = "GPL"
__version__ = "$Revision: 12903 $"

def _(s) : return s

from file import File
import os

def find(path=None,condition=lambda x : 1, precondition=lambda x : 1,dereference=False) :
    """ 
        Return file items satisfyed condition, if directory estimation by precondition
        is false this directory will be skipped from run.

        >>> import pd.find
        >>> pd.find.find("/etc/sysconfig",lambda x : x.isreg() and x.check_regex(".*rc"))
        <generator object at 0xb7cca7cc>
        >>> for item in pd.find.find("/etc/sysconfig",lambda x : x.isreg() and x.check_regex(".*rc$")) : 
        ... print item.path
        ...
        /etc/sysconfig/xinitrc
        /etc/sysconfig/syscheckerrc
        >>>

    """
    queue = [File(path,dereference=dereference)]
    while(queue) :
        item = queue.pop()
        
        if precondition(item) :
            if item.isdir() :
                queue.extend(item.values())
                
            if condition(item) :
                yield item
                
if  __name__ == '__main__' :
    print "Lads, it's only module, don't use it as application..."
