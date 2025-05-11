const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split(/\s+/).map(Number);
let idx = 0;
const n = input[idx++];
const A = new Int32Array(n + 1);
for (let i = 1; i <= n; ++i) A[i] = input[idx++];
const s = input[idx];
const visited = new Uint8Array(n + 1);
const queue = new Int32Array(n + 5);
let head = 0, tail = 0;
visited[s] = 1;
queue[tail++] = s;
let count = 1;

while (head < tail) {
  const cur = queue[head++];
  const jump = A[cur];

  const left = cur - jump;
  if (left >= 1 && !visited[left]) {
    visited[left] = 1;
    queue[tail++] = left;
    ++count;
  }

  const right = cur + jump;
  if (right <= n && !visited[right]) {
    visited[right] = 1;
    queue[tail++] = right;
    ++count;
  }
}

console.log(count.toString());