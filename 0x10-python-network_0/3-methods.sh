#!/bin/bash
# Send an OPTIONS request to the URL and display the Allow header
curl -s -X OPTIONS -i "$1" | grep -i 'Allow' | cut -d':' -f2 | tr -d '[:space:]'
