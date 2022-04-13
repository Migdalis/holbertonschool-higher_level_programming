#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = {};
    const listAll = JSON.parse(body);
    for (const element of listAll) {
      if (element.completed === true) {
        if (element.userId in data) {
          data[element.userId] += 1;
        } else {
          data[element.userId] = 1;
        }
      }
    }
    console.log(data);
  }
});
