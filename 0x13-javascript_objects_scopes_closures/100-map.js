#!/usr/bin/node

const dataList = require('./100-data').list;

const listMap = dataList.map((element, i) => element * i);
console.log(dataList);
console.log(listMap);
