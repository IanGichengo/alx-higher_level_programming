#!/usr/bin/node

const fs = require('fs')

function readAndPrintFile (filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf-8')
    console.log(content)
  } catch (error) {
    console.error(`Error: ${error.message}`)
  }
}

if (process.argv.length !== 3) {
  console.error('Usage: node script_name.js <file_path>')
  process.exit(1)
}

const filePath = process.argv[2]
readAndPrintFile(filePath)
