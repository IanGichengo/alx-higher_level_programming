#!/usr/bin/node
const request = require('request');
function getCharacterName (url) {
  request(url, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const data = JSON.parse(body);
      console.log(data.name);
    }
  });
}
function getMovieCharacters (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  request(url, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const data = JSON.parse(body);
      data.characters.forEach(getCharacterName);
    }
  });
}
getMovieCharacters(3);
