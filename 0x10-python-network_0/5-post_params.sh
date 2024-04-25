#!/bin/bash
# Send a POST request to the URL with two variables and display the body response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
