#!/bin/bash
# Script that sends a DELETE request to the URL passed and displays the body of the response
curl -sLX "DELETE" "$1"
