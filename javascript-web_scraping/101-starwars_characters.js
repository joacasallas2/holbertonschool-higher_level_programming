#!/usr/bin/node
// Print all characters of a Star Wars movie
const request = require('request');
const args = process.argv;
if (args.length < 3) {
  console.error('Usage must be: ./100-starwars_characters.js <number>');
  process.exit(1);
}
const movieNumber = process.argv[2];
const urlMovie = `https://swapi-api.hbtn.io/api/films/${movieNumber}`;

request(urlMovie, function (error, response, body) {
  if (error) {
    console.error('error:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error('Error: fetching data');
    return;
  }
  try {
    const data = JSON.parse(body);
    const characters = data.characters;
    for (const charUrl of characters) {
      request(charUrl, function (charError, charResponse, charBody) {
        if (charError) {
          console.error('error:', charError);
          return;
        }
        if (charResponse.statusCode !== 200) {
          console.error('Error: fetching data character');
          return;
        }
        try {
          const dataCharacter = JSON.parse(charBody);
          console.log(dataCharacter.name);
        } catch (charParseError) {
          console.error('Error parsing JSON:', charParseError);
        }
      });
    }
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
