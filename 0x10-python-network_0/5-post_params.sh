#!/bin/bash
# Send a POST request with specific variables in the request body and display the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"