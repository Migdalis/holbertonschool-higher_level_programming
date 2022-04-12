#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const id = 18;

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const listFilms = JSON.parse(body).results;
    const character = 'https://swapi-api.hbtn.io/api/people/' + id + '/';
    let count = 0;
    for (const element of listFilms) {
      if (element.characters.includes(character)) {
        count++;
      }
    }
    console.log(count);
  }
});
