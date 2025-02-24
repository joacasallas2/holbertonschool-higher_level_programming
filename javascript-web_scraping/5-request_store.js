#!/usr/bin/node
// Get the contents of a webpage and stores it in a file.
const fs = require('fs');
const request = require('request');
const args = process.argv;
const len = args.length;
if (len < 4) {
  console.error('Usage must be ./5-request_store.js <url> <filepath>');
  process.exit(1);
}
const url = args[2];
request(url, function (error, response, body) {
  if (error) {
    console.error('error: ', error);
    process.exit(1);
  }
  if (response.statusCode !== 200) {
    console.error('Error fetching content');
    process.exit(1);
  }
  try {
    fs.writeFileSync(args[3], body);
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
