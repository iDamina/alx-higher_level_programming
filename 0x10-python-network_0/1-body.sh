#!/bin/bash
# Send a GET request and display the body if the status code is 200
response=$(curl -s -o /dev/null -w "%{http_code}" "$1"); [ "$response" -eq 200 ] && curl -s "$1" || echo $response
