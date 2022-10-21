#!/bin/bash
# the server responds with 'You got me!' when the url below is loaded
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H 'Origin:HolbertonSchool'
