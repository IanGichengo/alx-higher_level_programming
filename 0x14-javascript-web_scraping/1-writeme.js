#!/usr/bin/node
const fs = require('fs');
function writeToFile (filePath, content) {
  try {
    fs.writeFileSync(filePath, content, 'utf-8');
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
}
if (process.argv.length !== 4) {
  console.error('Usage: node script_name.js <file_path> <string_to_write>');
  process.exit(1);
}
const filePath = process.argv[2];
const content = process.argv[3];
writeToFile(filePath, content);
