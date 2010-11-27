# -*- coding: utf-8 -*-

__doc__ = """\
Project:    Python Find
Version:    $Id: __init__.py 12910 2007-11-10 19:09:37Z cray $
Licence:    GPL
Start:      Sat Jun  5 09:42:53 MSD 2004
Title:      Python Find / Init
Author:     
    Andrey Orlov (c) 2004
        
Description:     

    Python Find is utility to use like shell "find" program for
    files finding and its treatment.
        
Warranty:

    There is no warranty of any kind, either expressed
    or implied
                        
TODO:
    Nothing

"""
__version__ = '$Rev: 1.1 $'[6:-1]
# $Id: __init__.py 12910 2007-11-10 19:09:37Z cray $
def _(s) : return s

from find import find
from file import File

if __name__ == '__main__' :
    print "Lads, it's only module, don't use it as application..."
    