#!/usr/bin/python3
"""
This module takes in a URL and an email address, sends a POST
request to the passed URL with the email as a parameter and
display the body of the response
"""
import sys
import requests

if __name__ == "__main__":
    url_input = sys.argv[1]
    email_input = sys.argv[2]
    data = {}
    data['email'] = email_input
    r = requests.post(url_input, data)
    print(r.text)
