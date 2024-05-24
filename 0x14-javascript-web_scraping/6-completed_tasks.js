#!/usr/bin/node
'use strict';
const request = require('request');
if (process.argv.length !== 3) {
  console.error('Usage: ./6-completed_tasks.js <API URL>');
  process.exit(1);
}
const apiUrl = process.argv[2];
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }
  if (response.statusCode !== 200) {
    console.error('Failed to retrieve data. Status code:',
      response.statusCode);
    process.exit(1);
  }
  const todos = JSON.parse(body);
  const completedTasks = {};
  todos.forEach(todo => {
    if (todo.completed) {
      if (!completedTasks[todo.userId]) {
        completedTasks[todo.userId] = 0;
      }
      completedTasks[todo.userId]++;
    }
  });
  console.log(completedTasks);
});
