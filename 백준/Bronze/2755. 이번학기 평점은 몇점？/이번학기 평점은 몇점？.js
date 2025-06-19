const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').toString().trim().split('\n');

const score = {
  'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
  'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
  'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
  'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
  'F': 0.0
};

const N = parseInt(input[0]);
let tredit = 0;
let tcore = 0;

for (let i = 1; i <= N; i++) {
  const [subject, creditStr, grade] = input[i].split(' ');
  const credit = parseInt(creditStr);
  const gpa = score[grade];

  tcore += credit * gpa;
  tredit += credit;
}

const temp = tcore / tredit;
const ans = Math.round(temp * 100) / 100;
console.log(ans.toFixed(2));