#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays the response"""
import requests
import sys

""" Get the URL from the command line arguments"""
if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
