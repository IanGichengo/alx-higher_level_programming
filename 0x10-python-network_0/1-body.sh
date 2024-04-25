#!/bin/bash
#takes in a URL, sends a GET request to the URL, and displays the body
curl -sL -w "%{http_code}" "$1" -o /dev/null | grep -q "200" && curl -s "$1"
