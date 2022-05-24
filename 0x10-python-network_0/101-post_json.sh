#!/bin/bash
# Script that sends a JSON POST request and displays the body of the response
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
