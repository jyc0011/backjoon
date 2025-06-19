const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').toString().trim().split('\n').map(Number);
const check = Array(31).fill(false);

for (let i = 0; i < input.length; i++) {
    check[input[i]] = true;
}

const ans = [];
for (let i = 1; i <= 30; i++) {
    if (!check[i]) ans.push(i);
}

console.log(ans[0]);
console.log(ans[1]);