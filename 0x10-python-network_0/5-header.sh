#!/bin/bash
# sets a header variable X-School-User-Id to 98
curl -s -H "X-School-User-Id: 98" "$1"
