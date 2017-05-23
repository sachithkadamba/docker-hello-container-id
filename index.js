var http = require("http");
var os = require("os");
var uuid = require('node-uuid');


http.createServer(function (request, response) {

   // Send the HTTP header
   // HTTP Status: 200 : OK
   // Content Type: text/plain
   response.writeHead(200, {'Content-Type': 'text/plain'});

   // Send the response body as "Hello World"
   response.end('Hello ' + os.hostname());
}).listen(8080);

console.log("Server running at port 8080");
