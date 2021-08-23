#!/bin/bash
# Sends a POST request to the passed URL, the variables email and subject
curl -sd 'email=hr@holbertonschool.com&subject=I will always be here for PLD' "$1"
