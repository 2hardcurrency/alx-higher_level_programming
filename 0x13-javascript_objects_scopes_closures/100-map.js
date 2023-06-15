#!/usr/bin/node
const list = require('./100-data');

// Computing the new array using map
const newList = list.map((value, index) => value * index);

// Printing the initial list
console.log('Initial List:');
console.log(list);

// Printing the new list
console.log('New List:');
console.log(newList);
