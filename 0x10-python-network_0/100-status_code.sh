#!/bin/bash
# Use curl to send a request and display only the status code
curl -s -L -X HEAD -w "%{http_code}" "$1"
