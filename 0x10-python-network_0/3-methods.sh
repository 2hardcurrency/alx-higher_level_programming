#!/bin/bash
# Write a Bash script that sends a DELETE request to to URL
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
