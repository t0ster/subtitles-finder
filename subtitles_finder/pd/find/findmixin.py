### -*- coding: utf-8 -*- #############################################
#######################################################################
"""Find provide a way to treatment file hierarhies and file sequence with
some conditional return.


$Id: findmixin.py 12910 2007-11-10 19:09:37Z cray $
"""
__author__  = "Andrey Orlov, 2004"
__license__ = "GPL"
__version__ = "$Revision: 12903 $"

def _(s) : return s

import stat,os
import re
import time

class FindMixIn(object) :
    """ Provide some methods used on file item """

    def __init__(self,path,**kw) :
        super(FindMixIn,self).__init__(path,**kw)

    def __checktime_(self,t) :
        return (time.time() - self.stat[t]) / 60 / 60 /24 

    def mtime(self) :
        """ Return modification time """
        return self.__checktime_(stat.ST_MTIME)
        
    def atime(self) :
        """ Return last access time """
        return self.__checktime_(stat.ST_ATIME)
        
    def ctime(self) :
        """ Return creation time """
        return self.__checktime_(stat.ST_CTIME)
        
    def newer(self,path) :
        """ Return true if object is more newer then input path """
        return os.stat(path)[self.ST_MTIME] > self.stat[stat.ST_MTIME]
    
    def check_name(self,name) :
        """ Return true if object name are equal to input name """
        return self.name == name

    def check_path(self,path) :
        """ Return true if object path are equal to input path """
        return self.path == path
        
    def check_path_regex(self,regexp) :
        """ Return true if regexp matched object path """
        return re.compile(regexp).match(self.path)

    def check_regex(self,regexp) :
        """ Return true if regexp matched object name """
        return re.compile(regexp).match(self.name)

    def check_iregex(self,regexp) :
        """ Return true if regexp matched object name """
        return re.compile(regexp,re.I).match(self.name)
        
    def depth(self) :
        """ Return current depth on file tree """
        return self._depth

    def dele(self) :
        """ Delete file by path of current object """
        os.remove(self.path)

    def execute(self,frm=None) :
        """ Frm will be substituted by substring "{}" on path and executed
        by os.system() call """

        if frm is not None :
            os.system(frm.replace("{}",self.path))
            
if __name__ == '__main__' :
    print "Lads, it's only module, don't use it as application..."
    