#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL and displays
the body of the response
"""
import requests
import sys

if __name__ == "__main__":
    url_input = sys.argv[1]
    r = requests.get(url_input)
    if (r.status_code >= 400):
        print("Error code:", r.status_code)
    else:
        print(r.text)
