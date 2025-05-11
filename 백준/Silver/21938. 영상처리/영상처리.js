const fs = require('fs');
const buf = fs.readFileSync(0, 'utf8').trim().split(/\s+/).map(Number);
let pos = 0;
const N = buf[pos++];
const M = buf[pos++];
const PIXELS = N * M;
const colors = buf.slice(pos, pos + 3 * PIXELS);
pos += 3 * PIXELS;
const T = buf[pos];
const bin = new Uint8Array(PIXELS);

for (let p = 0, i = 0; i < PIXELS; ++i, p += 3) {
  const avg = (colors[p] + colors[p + 1] + colors[p + 2]) / 3;
  bin[i] = avg >= T ? 1 : 0;
}

const q = new Uint32Array(PIXELS);
const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];
let head = 0, tail = 0, cnt = 0;

for (let r = 0; r < N; ++r) {
  for (let c = 0; c < M; ++c) {
    const start = r * M + c;
    if (bin[start] === 0) continue;
    ++cnt;
    bin[start] = 0;
    q[tail++] = start;

    while (head < tail) {
      const cur = q[head++];
      const x = (cur / M) | 0;
      const y = cur % M;

      for (let k = 0; k < 4; ++k) {
        const nx = x + dx[k];
        const ny = y + dy[k];
        if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;

        const idx = nx * M + ny;
        if (bin[idx]) {
          bin[idx] = 0;
          q[tail++] = idx;
        }
      }
    }
  }
}

console.log(cnt.toString());