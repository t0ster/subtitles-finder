#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import imp
import argparse

from subtitles_finder.media_finder import find_media_files
from subtitles_finder.srt_scrapper import get_srt, SubtitlesNotFoundError

HELP = \
"""
You have to create settings.py file. Here is example:

# -*- coding: utf-8 -*-
TV_SHOWS_DIRS = (
    '/Volumes/My Media/My Video/My TV Shows',
)
EXCLUDE_DIRS = (
    '/Volumes/My Meida/My Video/My TV Shows/Star Trek',
    '/Volumes/My Media/My Video/My TV Shows/Futurama/Футурама',
)
"""


def main():
    args = parse_args()
    settings = imp.load_source('settings', args.settings)

    media_files = find_media_files(
        settings.TV_SHOWS_DIRS, settings.EXCLUDE_DIRS)
    for tv_show, season, episode, path in media_files:
        srt_path = re.sub(r'(.+)\..+$', '\\1.srt', path)
        if os.path.exists(srt_path) and not args.fetch_existing:
            print "Already have subtitles for %s %sx%s" % (
                tv_show, season, episode)
            continue
        print "Getting subtitles for %s %sx%s" % (tv_show, season, episode)
        try:
            srt = get_srt(tv_show, season, episode)
        except SubtitlesNotFoundError as e:
            print e.args[0]
            continue
        with open(srt_path, 'w+') as f:
            f.write(srt)
        print "Got %s" % srt_path


def parse_args():
    parser = argparse.ArgumentParser(
        description="Scans your filesystem for TV Shows, "
        "than tries to find subtitles",
        epilog=HELP,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('settings', metavar='settings_file', type=str,
                        help='path to settings file. (example: ~/settings.py)')
    parser.add_argument(
        '-f', '--fetch-existing', dest='fetch_existing', action='store_true',
        help='fetch subtitles that we already have (default: don\'t)')

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    main()
