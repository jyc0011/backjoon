const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\n');

const M = 1234567891;
const r = 31;
const L = Number(input[0]);
const str = input[1];

let result = 0;
let power = 1;

for (let i = 0; i < L; i++) {
    const ch = str.charCodeAt(i) - 96;
    result = (result + (ch * power) % M) % M;
    power = (power * r) % M;
}

console.log(result);