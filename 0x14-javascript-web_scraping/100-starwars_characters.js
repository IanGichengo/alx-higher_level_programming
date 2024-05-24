#!/usr/bin/node
'use strict';
const request = require('request');
if (process.argv.length !== 3) {
  console.error('Usage: ./100-starwars_characters.js <Movie ID>');
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
  const film = JSON.parse(body);
  const characters = film.characters;
  characters.forEach(characterUrl => {
    request.get(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
        return;
      }
      if (charResponse.statusCode !== 200) {
        console.error('Failed to retrieve character. Status code:', charResponse.statusCode);
        return;
      }
      const character = JSON.parse(charBody);
      console.log(character.name);
    });
  });
});
