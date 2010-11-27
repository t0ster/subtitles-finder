### -*- coding: utf-8 -*- #############################################
#######################################################################
"""Find provide a way to treatment file hierarhies and file sequence with
some conditional return.


$Id: filewrapper.py 12910 2007-11-10 19:09:37Z cray $
"""
__author__  = "Andrey Orlov, 2004"
__license__ = "GPL"
__version__ = "$Revision: 12903 $"

def _(s) : return s

import stat,os,sys

class FileWrapper(object) :
    """ Base File Wrapper """
    
    def __init__(self,path,dereference=False,depth=0,**kw) :
        """ Init file """
        self.name = os.path.basename(path)
        self.path = path
        self.dereference = dereference
        self._depth=depth
        self.kw = kw.copy()
        
        if dereference :
            self.stat = os.stat(path)
        else :
            self.stat = os.lstat(path)

    def isreg(self) :
        """ Return true if is it regular file """
        return stat.S_ISREG(self.stat[0])

    def isdir(self) :
        """ Return true if is it directory file """
        return stat.S_ISDIR(self.stat[0])

    def keys(self) :
        """ Return keys (names) in direcory """
        if not self.isdir() :
            raise OSError
            
        return os.listdir(self.path)

    def items(self) :
        """ Return directory items """
        return [ (item, self[item]) for item in self.keys() ]

    def values(self) :
        """ Return directory values """
        return [ value for key,value  in self.items() ]
        
    def has_key(self,key) :
        """ Return True if directory has key """
        return os.path.exists(os.path.join(self.path,key))

    def __getitem__(self,key) :
        """ Get value by this key """
        return self.__class__(os.path.join(self.path,key),self.dereference,depth=self._depth+1,**self.kw)
        
    def __setitem__(self,key) :
        raise OSError

    def __delitem__(self,key) :
        raise OSError
    
    def __len__(self) :
        """ Return dir length """
        return len(os.listdir(self.path))

    def __repr__(self) :
        return repr(self.path)
        
    def __str__(self) :
        """ Return string presentation of File """
        if self.isdir() :
            return '\n---------------\n'.join([ str(x) for x in self.values()])
        else :
            try :
                return open(self.path).read()
            except (IOError,OSError) :
                return '' 
                
if __name__ == '__main__' :
    print "Lads, it's only module, don't use it as application..."
    
