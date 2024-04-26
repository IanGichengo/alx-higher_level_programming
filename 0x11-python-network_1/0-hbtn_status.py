#!/usr/bin/python3
# Import the required module
import urllib.request

# Define the URL
url = "https://alx-intranet.hbtn.io/status"

# Use urllib to open the URL
with urllib.request.urlopen(url) as response:
    # Read the response
    html = response.read()
    # Print the response
    print("Body response:")
    print("\\t- type: {}".format(type(html)))
    print("\\t- content: {}".format(html))
    print("\\t- utf8 content: {}".format(html.decode('utf-8')))
