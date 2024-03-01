#!/bin/bash
# script that takes a url, sends a request and displays the size of the body
url=$1; mes_bdy=$(curl -sI "$url" | awk -v RS='\r?\n' '/Content-Length:/ {print $2}'); echo $mes_bdy
