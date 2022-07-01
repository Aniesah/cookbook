/*
  app-express.js
  First web server with Express
  
  url https://nodejs.dev/learn/how-to-exit-from-a-nodejs-program
  [20220511].
*/
const express = require('express');

const app = express();

app.get('/', (req, res) => {
  res.send('Hi!');
});

const server = app.listen(3000, () => console.log('Server ready'));

process.on('SIGTERM', () => {
  server.close(() => {
    console.log('Process terminated');
  });
});