const fs = require('fs');
const [A, B] = fs.readFileSync(0, 'utf8').trim().split(' ').map(Number);
const result = (A + B) * (A - B);
console.log(result);