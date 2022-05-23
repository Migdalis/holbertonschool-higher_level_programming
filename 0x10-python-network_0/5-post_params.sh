#!/bin/bash
# Script that sends a POST request, and displays the body of the response
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
