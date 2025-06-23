const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split('\n');

const N = Number(input[0]);
const scores = input[1].split(' ').map(Number);

const m = Math.max(...scores);
const n = scores.map(score => (score / m) * 100);
const avg = n.reduce((a, b) => a + b, 0) / N;
const ans = Number(avg.toFixed(6));
if (Number.isInteger(ans)) {
  console.log(ans.toFixed(1));
} else {
  console.log(ans);
}