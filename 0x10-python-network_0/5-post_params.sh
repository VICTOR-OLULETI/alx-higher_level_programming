#!/bin/bash
# sends a POST request to the passed URL
curl -s -F 'email=test@gmail.com;subject="I will always be here for PLD"' "$1"
