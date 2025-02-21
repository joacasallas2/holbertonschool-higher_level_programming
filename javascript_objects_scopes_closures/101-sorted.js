#!/usr/bin/node
/* Import a dict of occurrences by user id and computes
a dict of user ids by occurrence.   */
const { dict } = require('./101-data');
const ocurrences = {};
for (const [userId, ocurrence] of Object.entries(dict)) {
  if (!(ocurrence in ocurrences)) {
    ocurrences[ocurrence] = [];
  }
  ocurrences[ocurrence].push(userId);
}
console.log(ocurrences);
