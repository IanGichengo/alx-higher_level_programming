#!/bin/bash
#sends a JSON POST request to a URL passed as the first argument and displays
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
