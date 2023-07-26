#!/usr/bin/node
const request = require('request-promise-native');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

function computeCompletedTasksByUserId(tasks) {
  const completedTasksByUser = {};

  tasks.forEach((task) => {
    if (task.completed) {
      if (!completedTasksByUser[task.userId]) {
        completedTasksByUser[task.userId] = 1;
      } else {
        completedTasksByUser[task.userId]++;
      }
    }
  });

  return completedTasksByUser;
}

function printUsersWithCompletedTasks(apiUrl) {
  request(apiUrl)
    .then((response) => {
      const tasks = JSON.parse(response);
      const completedTasksByUser = computeCompletedTasksByUserId(tasks);

      for (const userId in completedTasksByUser) {
        console.log(`User ID ${userId} completed ${completedTasksByUser[userId]} tasks.`);
      }
    })
    .catch((err) => {
      console.error('Error occurred:', err);
    });
}

printUsersWithCompletedTasks(apiUrl);
