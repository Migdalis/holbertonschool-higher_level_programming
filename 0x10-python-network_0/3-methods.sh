#!/bin/bash
# Script that takes in a URL and displays all HTTP methods the server will accept
curl -siX OPTIONS "$1" | grep "Allow: " | cut -b 8-
