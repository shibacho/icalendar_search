#!/usr/bin/env python
# -*- coding: utf-8 -*-

import icalendar_search

def main():
    cal = icalendar_search.CalendarSearch()

    ### example.ics(日本の祝日カレンダー) をロードする
    ### load example.ics(Japanese Holidays)
    cal.load('example.ics')

    ### 「日」という文字が含まれる予定を検索する
    ### Find the events including '日'
    results = cal.search(u'日')

    ### それぞれの検索結果を表示する
    ### 検索結果の文字列はunicode文字列で帰ってくることに注意
    ### Show each results.
    ### Note that each results summary is unicode string.
    for a_result in results:
        print "%s -> %s: %s" % (a_result.start_time.strftime('%Y/%m/%d %H:%M:%S'),
                                a_result.end_time.strftime('%Y/%m/%d %H:%M:%S'),
                                a_result.summary.encode('Shift_JIS')) ### for Windows
###                             a_result.summary.encode('EUC_JP'))    ### for Linux 
###                             a_result.summary.encode('utf-8'))

if __name__ == '__main__':
    main()

