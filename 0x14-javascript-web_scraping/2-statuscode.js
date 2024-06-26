#!/usr/bin/node
'use strict';
const request = require('request');
if (process.argv.length !== 3) {
  console.error('Usage: ./2-statuscode.js <URL>');
  process.exit(1);
}
const url = process.argv[2];
request.get(url, (error, response) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }
  console.log(`code: ${response.statusCode}`);
});
