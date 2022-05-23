#!/bin/bash
# Script that sends a GET request to a URL, and displays the body of the response
curl -X GET "$1" -H "X-HolbertonSchool-User-Id: 98"
