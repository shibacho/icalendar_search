# -*- coding: utf-8 -*-
# Copyright (C) 2011 by fantakeshi 
# Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php
# Author: fantakeshi
# Contact: fantakeshi1@gmail.com
# It follows the ``RFC 2445 http://www.ietf.org/rfc/rfc2445.txt (iCalendar) specification`` (as a part)

__author__ = 'fantakeshi1@gmail.com'
__version__ = '0.1'

import datetime
import re

import sys

class CalendarSearch(object):
    """
    This is searching module for icalendar by a unicode string.
    This module focuses on just searching, not creating event, or etc...
    """
    def __init__(self):
        self._path = ''
        self._event_list = []

    def load(self, path, encoding = 'utf-8'):
        self._path = path
        f = open(path)
        string = f.read()
        f.close()
        self._parse_string(string, encoding)
        return self

    def load_from_url(self, url):
        self._path = url
        ### TODO:Not Implemented:
        return self

    def clear(self):
        self._event_list = []

    def get_datetime_from_dtstr(self, string):
        search = re.compile(r':(\d{4})(\d{2})(\d{2})T(\d{2})(\d{2})(\d{2})').search(string)

        if search is not None:
            return datetime.datetime(int(search.group(1)),
                                     int(search.group(2)),
                                     int(search.group(3)),
                                     int(search.group(4)),
                                     int(search.group(5)),
                                     int(search.group(6)))
        else:
            search = re.compile(r':(\d{4})(\d{2})(\d{2})').search(string)
            return datetime.datetime(int(search.group(1)),
                                     int(search.group(2)),
                                     int(search.group(3)))


    def _parse_string(self, string, encoding = 'utf-8'):
        event = None
        for line in string.splitlines():
            if line.find('BEGIN:VEVENT') >= 0:
                event = CalendarEvent()
            elif line.find('END:VEVENT') >= 0:
                self._event_list.append(event)
            elif line.find('DTSTART') >= 0:
                event.start_time = self.get_datetime_from_dtstr(line)
            elif line.find('DTEND') >= 0:
                event.end_time = self.get_datetime_from_dtstr(line)
            elif line.find('CREATED:') >= 0:
                event.created = self.get_datetime_from_dtstr(line)
            elif line.find('LAST-MODIFIED:') >= 0:
                event.last_modified = self.get_datetime_from_dtstr(line)
            elif line.find('SUMMARY:') >= 0:
                line = unicode(line, encoding)
                index = len('SUMMARY:')
                event.summary = line[index:]
            elif line.find('DESCRIPTION:') >= 0:
                line = unicode(line, encoding)
                index = len('DESCRIPTION:')
                event.description = line[index:]

    """
    Search Calendar by a unicode string.
    This function uses a linear search so complexity is O(n).
    :param: uni_string: The search unicode string.
    """
    def search(self, uni_string):
        regex = re.compile(uni_string, re.U)
        result_list = []
        for event in self._event_list:
            if regex.search(event.summary):
                result_list.append(event)
            elif regex.search(event.description):
                result_list.append(event)
        return result_list

class CalendarEvent(object):
    """
    Each search result entry.
    :param: start_time    Start time (datetime object)
    :param: end_time      End   time (datetime object)
    :param: summary       Event summary (string)
    :param: description   Event description (string)
    :param: created       Event created time (datetime object)
    :param: last_modified Event Last Modified time (datetime object)
    """
    def __init__(self, start_time=None, end_time=None, 
                 summary = '', description = '',
                 created = None, last_modified = None):
        self.start_time = start_time
        self.end_time = end_time
        self.summary = summary
        self.description = description
        self.created = created
        self.last_modified = last_modified


import unittest
class CalendarSearchTest(unittest.TestCase):
    def setUp(self):
        self._calendar_search = CalendarSearch()
            
    def testLoadFile(self):
        self.assertRaises(TypeError, self._calendar_search.load, (1,2,3))
        self.assertRaises(IOError, self._calendar_search.load, 'http://www.google.com')
        self.assert_(self._calendar_search.load('test.ics'))
                
    def testClear(self):
        self._calendar_search.clear()
        self.assertEqual(self._calendar_search.search('a'), [])
        self.assertEqual(self._calendar_search.search(u'あ'), [])
        self.assertEqual(self._calendar_search.search(u'日'), [])
                    
    def testSearch(self):
        self.assert_(self._calendar_search.load('test.ics'))
        self.assertNotEqual(self._calendar_search.search(u'日'), [])
        results = self._calendar_search.search(u'日')
        self.assertEqual(len(results), 48)
                
### below the test code.
if __name__ == '__main__':
                
    unittest.main()
