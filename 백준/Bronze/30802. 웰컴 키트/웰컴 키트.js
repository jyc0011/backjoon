const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\n');

const N = parseInt(input[0]);
const sizes = input[1].split(' ').map(Number); // [S, M, L, XL, XXL, XXXL]
const [T, P] = input[2].split(' ').map(Number);

let t = 0;
for (let i = 0; i < sizes.length; i++) {
  t += Math.floor((sizes[i] + T - 1) / T);
}

const p = Math.floor(N / P);
const i = N % P;

console.log(t);
console.log(p, i);
