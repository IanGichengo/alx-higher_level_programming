#!/bin/bash
#takes in a URL, sends a GET request to the URL, and displays the body
curl -s -w "%{http_code}" "$1" -o response.txt | { read status; [ "$status" -eq 200 ] && cat response.txt; }
