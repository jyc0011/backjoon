const fs = require('fs');
const N = parseInt(fs.readFileSync(0, 'utf8').trim());
let cnt = 1;
let maxN = 1;
while (N > maxN) {
  maxN += 6 * cnt;
  cnt++;
}

console.log(cnt);