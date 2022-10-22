#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL and displays
the body of the response(decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse
import urllib.error

if __name__ == "__main__":
    url_input = sys.argv[1]
    req = urllib.request.Request(url_input)

    try:
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
            print(the_page.decode("utf-8"))
    except urllib.error.URLError as e:
        print('Error code: ', e.code)
