#!/usr/bin/node
const dataList = require('./100-data.js').list;
console.log(dataList);
console.log(dataList.map((item, index) => item * index));
