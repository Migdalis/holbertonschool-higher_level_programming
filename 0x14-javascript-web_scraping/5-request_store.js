#!/usr/bin/node

const file = require('fs');
const request = require('request');
const url = process.argv[2];

request(url).pipe(file.createWriteStream(process.argv[3]));
