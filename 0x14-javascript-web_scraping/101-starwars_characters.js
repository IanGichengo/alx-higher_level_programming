#!/usr/bin/node
const axios = require('axios');
async function getCharacterName (url) {
  const response = await axios.get(url);
  return response.data.name;
}
async function printCharacters (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  const response = await axios.get(url);
  const data = response.data;
  for (const characterUrl of data.characters) {
    const name = await getCharacterName(characterUrl);
    console.log(name);
  }
}
printCharacters('3');
