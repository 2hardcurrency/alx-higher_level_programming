#!/usr/bin/node
import { dict } from './101-data.js';

function computeUserIdsByOccurrences(dict) {
  const userIdsByOccurrences = {};

  for (const [occurrences, userIds] of Object.entries(dict)) {
    if (!userIdsByOccurrences.hasOwnProperty(occurrences)) {
      userIdsByOccurrences[occurrences] = [];
    }

    userIdsByOccurrences[occurrences] = userIdsByOccurrences[occurrences].concat(userIds);
  }

  return userIdsByOccurrences;
}

const userIdsByOccurrences = computeUserIdsByOccurrences(dict);
console.log(userIdsByOccurrences);
