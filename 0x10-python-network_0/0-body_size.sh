#!/bin/bash
# Script that display the size of the a body response
curl -sI "$1" | grep "Content-Length: " | cut -b 17-
