### -*- coding: utf-8 -*- #############################################
#######################################################################
"""Common file object


$Id: file.py 12910 2007-11-10 19:09:37Z cray $
"""
__author__  = "Andrey Orlov, 2004"
__license__ = "GPL"
__version__ = "$Revision: 12903 $"

def _(s) : return s

import stat,os,sys

import posixmixin
import findmixin, filewrapper

class File(posixmixin.PosixMixIn,findmixin.FindMixIn,filewrapper.FileWrapper) :
    """ 
        Common file and directory wrapper 
        >>> import pd.find
        >>> f=pd.find.file.File("/etc/sysconfig")
        >>> f
        '/etc/sysconfig'
        >>> f.keys()
        ['harddisk', 'lm_sensors', 'ipw3945d~', 'syscheckerrc', 'mouse']
        >>> f['lm_sensors']
        '/etc/sysconfig/lm_sensors'
        >>> print str(f['lm_sensors'])
        #    /etc/sysconfig/lm_sensors - Defines modules loaded by
    """
    def __init__(self,path,dereference=False,**kw) :
        super(File,self).__init__(path,**kw)

if __name__ == '__main__' :
    print "Lads, it's only module, don't use it as application..."

