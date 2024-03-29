#!/usr/bin/node
/* print all characters of Star wars */

const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}/`;

request(url, (err, res, body) => {
  if (err) console.log(err);
  const index = 0;
  const cha = JSON.parse(body).characters;
  printData(cha, index);
});

const printData = function (url, i) {
  request(url[i], (err, res, body) => {
    if (err) console.log(err);
    console.log(JSON.parse(body).name);
    if (++i < url.length) {
      printData(url, i++);
    }
  });
};
