#!/usr/bin/node
// Print all characters of a Star Wars movie in the right order
const rp = require('request-promise');

const args = process.argv;

if (args.length < 3) {
  console.error('Usage must be: ./101-starwars_characters.js <number>');
  process.exit(1);
}

const movieNumber = process.argv[2];
const urlMovie = `https://swapi-api.hbtn.io/api/films/${movieNumber}`;

const fetchJson = (url) => rp({ url, json: true });

fetchJson(urlMovie)
  .then((data) => {
    const characterUrls = data.characters;
    return characterUrls.reduce((promise, url) => {
      return promise.then(() =>
        fetchJson(url).then((charData) => console.log(charData.name))
      );
    }, Promise.resolve());
  })
  .catch((error) => console.error('Error:', error.message));
