#!/usr/bin/node
// Compute the number of tasks completed by user id
const request = require('request');
const args = process.argv;
const len = args.length;

if (len < 3) {
  console.error('Usage must be ./6-completed_tasks.js <url>');
  process.exit(1);
}
const url = args[2];
request(url, function (error, response, body) {
  if (error) {
    console.error('error: ', error);
    process.exit(1);
  }
  if (response.statusCode !== 200) {
    console.error('Error fetching URL');
    process.exit(1);
  }
  try {
    const data = JSON.parse(body);
    const dictUsers = {};
    for (const obj of data) {
      if (!(obj.userId in dictUsers)) {
        dictUsers[obj.userId] = 0;
      }
      if (obj.completed === true) {
        dictUsers[obj.userId] += 1;
      }
    }
    for (const userId in dictUsers) {
      if (dictUsers[userId] === 0) {
        delete dictUsers[userId];
      }
    }
    console.log(dictUsers);
  } catch (parseError) {
    console.log('error parsing JSON: ', parseError);
  }
});
