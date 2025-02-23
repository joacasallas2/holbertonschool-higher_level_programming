#!/usr/bin/node
// Print the number of movies where the character “Wedge Antilles” is present.
const request = require('request');
const args = process.argv;
const len = args.length;
if (len < 3) {
  console.error('Usage must be ./4-starwars_count.js <url>');
  process.exit(1);
}
const url = args[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error('Error: Unable to fetch data from API');
    return;
  }
  try {
    let count = 0;
    const data = JSON.parse(body);
    data.results.forEach(film => {
      film.characters.forEach(character => {
        if (character.endsWith('/18/')) {
          count += 1;
        }
      });
    });
    console.log(count);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
