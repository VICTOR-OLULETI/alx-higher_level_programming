#!/usr/bin/python3
"""This module uses basic Authentications
"""
import sys
import requests
import requests.auth

if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    basic = requests.auth.HTTPBasicAuth(user, pwd)
    r = requests.get('https://api.github.com/user', auth=basic)
    print(r.json().get('id'))
