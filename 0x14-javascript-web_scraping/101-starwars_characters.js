#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2] + '/';

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const listPeople = JSON.parse(body).characters;
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
});
