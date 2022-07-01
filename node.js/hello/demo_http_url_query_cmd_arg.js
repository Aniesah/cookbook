/*
  demo_http_url_query_cmd_arg.js
  Read query string and command line arguments
  
  url https://www.w3schools.com/nodejs/nodejs_http
  .asp [20220511].
  url https://nodejs.dev/learn/nodejs-accept-arguments
  -from-the-command-line [20220512].
*/

process.argv.forEach((val, index) => {
  console.log(`${index}: ${val}`);
});

var http = require('http');
http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.write(req.url);
  res.end();
}).listen(8080);