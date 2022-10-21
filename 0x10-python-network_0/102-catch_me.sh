#!/bin/bash
# the server responds with 'You got me!' when the url below is loaded
curl -s -L -X PUT 0.0.0.0:5000/catch_me -d "You got me!"
