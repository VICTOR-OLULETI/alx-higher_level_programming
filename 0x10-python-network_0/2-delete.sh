#!/bin/bash
# sends a DELETE request to the URL passed as 1st argument
curl -s -L -X DELETE "$1"
