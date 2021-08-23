#!/bin/bash
# Sends a request to URL and displays the size of the body
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
