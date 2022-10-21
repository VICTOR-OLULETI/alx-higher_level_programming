#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL and
displays the value of the X-Request-Id
"""
import sys
import urllib.request

if __name__ == "__main__":
    url_input = sys.argv[1]
    req = urllib.request.Request(url_input)
    with urllib.request.urlopen(req) as response:
        print(response.headers.get('X-Request-Id'))
