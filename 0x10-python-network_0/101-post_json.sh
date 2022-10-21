#!/bin/bash
# using post method on a json type file
curl -s -X POST "$1" -H 'Content-Type:application/json' -d "@$2"
