#!/usr/bin/node
const occurencesDict = require('./101-data').dict;

const userIdsByOccurence = {};

for (const userID in occurencesDict) {
  const occurences = occurencesDict[userID];

  if (userIdsByOccurence[occurences]) {
    userIdsByOccurence[occurences].push(userID);
  } else {
    userIdsByOccurence[occurences] = [userID];
  }
}

console.log(userIdsByOccurence);
