#!/usr/bin/python3
"""This module takes 2 arguments in order to solve this challenge
"""
import sys
import requests
import requests.auth

if __name__ == "__main__":
    repos = sys.argv[1]
    name = sys.argv[2]
    url_input = 'https://api.github.com/repos/'+name+'/'+repos+'/commits'
    r = requests.get(url_input)
    r_dict = r.json()
    j = 0
    for i in (r_dict):
        if j < 10:
            j = j + 1
            print("{}: {} {}".format(i.get('sha'),
                  i.get('commit').get('author').get('name')))
        else:
            break
