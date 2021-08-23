#!/bin/bash
# Sends a JSON POST request to a URL and displays the body of the response
curl -sXH POST 'Content-Type: application/json' -d @"$2" "$1"
