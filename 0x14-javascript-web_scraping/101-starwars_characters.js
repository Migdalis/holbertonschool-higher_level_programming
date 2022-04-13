#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/';

request('https://swapi-api.hbtn.io/api/films/', (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const listFilms = JSON.parse(body).results;
    for (const film of listFilms) {
      if (film.url.include(process.argv[2])) {
        const listPeople = film.characters;
        for (const people of listPeople) {
          request(people, (error, response, body) => {
            if (error) {
              console.log(error);
            } else {
              console.log(JSON.parse(body).name);
            }
          });
        }
      }
    }
    
  }
});
