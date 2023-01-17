#!/usr/bin/node

const fs = require("fs");
const filename = process.argv[2];

fs.readFile(filename, "utf-8", (er, body) => {
  if (er) {
    console.log(er);
  } else {
    console.log(body);
  }
});
