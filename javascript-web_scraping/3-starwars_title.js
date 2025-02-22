#!/usr/bin/node
// Print the title of a Star Wars movie
// where the episode number matches a given integer.
const request = require('request');
const movieNumber = process.argv[2];
if (isNaN(movieNumber)) {
  console.error('Usage must be: ./3-starwars_title.js <number>');
  process.exit(1);
}
const url = `https://swapi-api.hbtn.io/api/films/${movieNumber}`;
request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error('Error: Invalid movie number:');
    return;
  }
  try {
    const data = JSON.parse(body);
    console.log(data.title);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
