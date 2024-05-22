#!/usr/bin/node
const http = require('http');
function getStatus (url) {
  const options = {
    method: 'GET',
    hostname: url,
    port: 80,
    path: '/'
  };
  const req = http.request(options, (res) => {
    console.log(`Status code: ${res.statusCode}`);
  });
  req.on('error', (error) => {
    console.error(`Error: ${error.message}`);
  });
  req.end();
}
getStatus('alx-intranet.hbtn.io/status');
getStatus('alx-intranet.hbtn.io/doesnt_exist');
