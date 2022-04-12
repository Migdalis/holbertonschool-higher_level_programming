#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const id = 18;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const listFilms = JSON.parse(body).results;
    let count = 0;
    for (const film of listFilms) {
      for (const char of film.characters) {
        if (char.includes(id)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
