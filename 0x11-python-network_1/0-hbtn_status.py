#!/usr/bin/python3
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'

try:
    with urllib.request.urlopen(url) as response:
        content_type: response.info().get_content_type()
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body.decode('utf-8'))
        print("\t- utf8 content:", body.decode('utf-8'))	
except urllib.error.URLError as e:
    print("Error:", e)
