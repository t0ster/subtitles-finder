# -*- coding: utf-8 -*-
"""
This module scans file system for TV Shows
"""
import re
import os
from re import compile as _

import pd.find


MEDIA_EXTENSIONS = ['avi', 'mkv', 'mov', 'mp4']
MEDIA_EXTENSIONS_REGEX = _(r'.+\.%s$' % '|'. join(MEDIA_EXTENSIONS))

# It should match:
#  Caprica.S01E13.rus.LostFilm.TV.avi
#  Футурама 1x01 - Space Pilot 3000.avi
#  South.Park.S14E14.Creme.Fraiche.HDTV.XviD-FQM.avi
TV_SHOW_REGEX = _(
    r'.+[^/]/(.+?)(?:.| )S?(\d{1,2})(?:x|х|E)(\d{1,2})',
    re.IGNORECASE
    )


def find_media_files(dirs, exclude_dirs=None):
    """
    Returns list of tuples (tv_show, season, episode, path)

    Arguments:
    - `dirs`: list of directories to search
    - `exclude_dirs`: list of directories to exclude
    """
    def condition(file_):
        return file_.isreg() and file_.check_regex(MEDIA_EXTENSIONS_REGEX)

    def precondition(file_):
        for dir_ in exclude_dirs:
            if dir_ in file_.path:
                return False
        return True

    if exclude_dirs is None:
        exclude_dirs = []
    result = []
    for dir_ in dirs:
        for file_ in pd.find.find(dir_, condition, precondition):
            m = re.match(TV_SHOW_REGEX, file_.path)
            if not m:
                print "Skipped %s" % file_.path
                continue
            tv_show, season, episode = m.groups()
            tv_show = tv_show.replace('.', ' ')
            result.append((tv_show, int(season), int(episode), file_.path))

    return result

if __name__ == '__main__':
    from pprint import pprint
    pprint(find_media_files(
            ['/Volumes/Someshit-1/My Video/TV Shows'],
            ['/Volumes/Someshit-1/My Video/TV Shows/Star Trek',
             '/Volumes/Someshit-1/My Video/TV Shows/Futurama/Футурама']))
