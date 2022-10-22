#!/usr/bin/python3
"""
This module takes in a URL and sends a request to the URL and
displays the value of the variable X-Request-Id
"""
import requests
import sys

if __name__ == "__main__":
    url_input = sys.argv[1]
    r = requests.get(url_input, auth=('user', 'pass'))
    print(r.headers['X-Request-Id'])
