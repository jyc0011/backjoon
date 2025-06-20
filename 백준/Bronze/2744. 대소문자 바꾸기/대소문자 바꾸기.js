const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim();

let result = '';

for (let ch of input) {
  if (ch >= 'a' && ch <= 'z') {
    result += ch.toUpperCase();
  } else if (ch >= 'A' && ch <= 'Z') {
    result += ch.toLowerCase();
  } else {
    result += ch;
  }
}

console.log(result);