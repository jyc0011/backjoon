const fs = require('fs');

const input = fs.readFileSync(0,'utf8').toString().split("\n");

const N = Number(input[0]);
const line = input[1].trim().split(' ').map(Number); 
const v = Number(input[2]);
let answer=0;

for(let i = 0; i < N; i++) {
  if (line[i] === v) answer++;

}

console.log(answer)