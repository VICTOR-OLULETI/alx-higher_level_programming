#!/usr/bin/python3
"""
This module fetches https://alx-intranet.hbtn.io/status using
requests library
"""
import requests
r = requests.get('https://alx-intranet.hbtn.io/status', auth=('user', 'pass'))
print("Body response:")
print("\t- type: {}".format(type(r.content.decode("utf-8"))))
print("\t- content: {}".format(r.content.decode("utf-8")))
