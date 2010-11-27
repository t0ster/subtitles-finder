# -*- coding: utf-8 -*-
# pylint: disable-msg=E1102
"""
This module searchs notabenoid.com site for subtitles

Usage:
>>> srt = get_srt('South Park', 14, 14)
>>> with open('~/subs.srt', 'w+') as f:
...     f.write(srt)
...
"""
import re

import mechanize

from subtitles_finder.utils import memoized


class SubtitlesNotFoundError(Exception):
    pass


@memoized
def get_srt(tv_show, season, episode):
    episode_regex = re.compile(
        r'%s.+%s.+%s' % (tv_show, season, episode),
        re.IGNORECASE)

    br = mechanize.Browser()
    br.open('http://notabenoid.com')
    br.select_form(nr=0)  # search form
    br['search_q'] = tv_show
    br.submit()

    try:
        br.follow_link(text_regex=episode_regex)
    except mechanize.LinkNotFoundError:
        raise SubtitlesNotFoundError(
            "Can't find subtitles for %s %sx%s" % (
                tv_show, season, episode))
    br.follow_link(text=u'»»»'.encode(br.encoding()))

    br.select_form(name='generator')
    br['enc'] = ['0']  # Кодировка utf-8
    # Пропускать варианты перевода с отрицательным рейтингом
    br['skip_neg'] = ['1']

    srt = br.submit()
    return srt.read()


if __name__ == '__main__':
    print get_srt('South Park', 14, 14)
