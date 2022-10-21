#!/bin/bash
# the server responds with 'You got me!' when the url below is loaded
curl -s -L 0.0.0.0:5000/catch_me -X PUT -H "Origin: You got me!"
