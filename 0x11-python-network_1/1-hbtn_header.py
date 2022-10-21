#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id
"""
import sys
import urllib.request

url_input = sys.argv[1]
req = urllib.request.Request(url_input)
with urllib.request.urlopen(req) as response:
    the_page = response.__dict__.get('headers')
    print(the_page.get('X-Request-Id'))
