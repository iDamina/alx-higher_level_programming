#!/bin/bash
# Send a GET request with a specific header and display the body of the response
curl -s -H "X-School-User-Id: 98" "$1"
