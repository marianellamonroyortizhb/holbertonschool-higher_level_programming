#!/bin/bash
# Makes a request to an URL and receive the message containing You got me!
curl -sL 0.0.0.0:5000/catch_me -X PUT -d 'user_id=98' -H 'Origin: HolbertonSchool'
