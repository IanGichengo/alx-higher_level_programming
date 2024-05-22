#!/usr/bin/node
'use strict';
const request = require('request');
if (process.argv.length !== 3) {
  console.error('Usage: ./3-starwars_title.js <movie ID>');
  process.exit(1);
}
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }
  if (response.statusCode !== 200) {
    console.error('Failed to retrieve data. Status code:', response.statusCode);
    process.exit(1);
  }
  const movieData = JSON.parse(body);
  console.log(movieData.title);
});
