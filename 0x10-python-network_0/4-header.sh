#!/bin/bash
# Send a GET request to the URL with a header variable and display the body
curl -sH "X-School-User-Id: 98" "$1"
