#!/usr/bin/python3
"""
This module takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response(decoded in utf-8)
"""
import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url_input = sys.argv[1]
    email_input = sys.argv[2]
    data = {}
    data['email'] = email_input
    url_values = urllib.parse.urlencode(data)
    url_values = url_values.encode('ascii')
    req = urllib.request.Request(url_input, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode("utf-8"))
