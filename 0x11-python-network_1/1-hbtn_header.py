#!/usr/bin/python3
"""script takes in a URL, sends a request to the URL, displays X-Request-Id"""
import urllib.request
import sys

""" Get the URL from the command line arguments """
url = sys.argv[1]

""" Send a request to the URL """
with urllib.request.urlopen(url) as response:
    headers = response.info()
    print(headers.get('X-Request-Id'))
