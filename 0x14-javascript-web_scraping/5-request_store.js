#!/usr/bin/node
/* store the content of a webpage in a file */

const request = require("request");
const fs = require("fs");
const url = process.argv[2];
const filename = process.argv[3];

request(url, (err, res, body) => {
  if (err) console.log(err);
  else {
    fs.writeFile(filename, body, "utf8", (err) => {
      if (err) console.log(err);
    });
  }
});
