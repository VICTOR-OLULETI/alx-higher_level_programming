#!/bin/bash
# takes a url, sends a request to the url and displays its size in bytes
curl -s "$1" | wc -c
