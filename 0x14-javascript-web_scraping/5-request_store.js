#!/usr/bin/node
'use strict';
const request = require('request');
const fs = require('fs');
if (process.argv.length !== 4) {
  console.error('Usage: ./5-request_store.js <URL> <file path>');
  process.exit(1);
}
const url = process.argv[2];
const filePath = process.argv[3];
request.get(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }
  if (response.statusCode !== 200) {
    console.error('Failed to retrieve data. Status code:',
      response.statusCode);
    process.exit(1);
  }
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error('Error writing to file:', err);
      process.exit(1);
    }
  });
});
