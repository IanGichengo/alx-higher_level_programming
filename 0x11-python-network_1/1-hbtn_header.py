#!/usr/bin/python3
import urllib.request
import sys

# Get the URL from the command line arguments
url = sys.argv[1]

# Send a request to the URL
with urllib.request.urlopen(url) as response:
    # Get the headers
    headers = response.info()
    # Print the value of the X-Request-Id variable
    print(headers.get('X-Request-Id'))
