#!/bin/bash
# Send a GET request with a specific header and display the body of the response
curl -s -H "X-School-User_Id: 98" "$1"
