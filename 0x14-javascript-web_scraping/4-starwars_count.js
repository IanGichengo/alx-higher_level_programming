#!/usr/bin/node
'use strict';
const request = require('request');
if (process.argv.length !== 3) {
  console.error('Usage: ./4-starwars_count.js <API URL>');
  process.exit(1);
}
const apiUrl = process.argv[2];
const wedgeAntillesId = '18';
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }
  if (response.statusCode !== 200) {
    console.error('Failed to retrieve data. Status code:',
      response.statusCode);
    process.exit(1);
  }
  const films = JSON.parse(body).results;
  let wedgeCount = 0;

  films.forEach(film => {
    film.characters.forEach(characterUrl => {
      if (characterUrl.includes(`/api/people/${wedgeAntillesId}/`)) {
        wedgeCount++;
      }
    });
  });
  console.log(wedgeCount);
});
