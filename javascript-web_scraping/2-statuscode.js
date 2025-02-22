#!/usr/bin/node
// display the status code of a GET request.
const request = require('request');
const args = process.argv;
const url = args[2];
if (args.length < 3) {
  console.error('Usage must be ./2-statuscode.js <url>');
  process.exit(1);
}
request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
    process.exit(1);
  }
  console.log(`code: ${response.statusCode}`);
});
