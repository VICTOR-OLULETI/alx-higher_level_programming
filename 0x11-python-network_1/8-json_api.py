#!/usr/bin/python3
"""This module works with json using the requests library
"""
import sys
import requests

if __name__ == "__main__":
    if (len(sys.argv) > 1):
        q = sys.argv[1]
    else:
        q = ""
    data = {}
    data['q'] = q
    r = requests.post('http://0.0.0.0:5000/search_user', data)
    res_type = r.headers['Content-Type']
    if (res_type == 'application/json'):
        r_dict = r.json()
        if (len(r_dict) == 0):
            print("No result")
        elif (r_dict.get('id') is not None):
            print("[{}] {}".format(r_dict.get('id'), r_dict.get('name')))
    else:
        print("Not a vaild JSON")
