#!/bin/bash
# Use curl to make a POST request to 0.0.0.0:5000/catch_me
curl -sL 0.0.0.0:5000/catch_me -X PUT -d "user_id=98" -H "Origin: HolbertonSchool"
