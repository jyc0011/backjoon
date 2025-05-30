const fs = require('fs');
let input = fs.readFileSync(0).toString().trim();

function change(letter) {
  if (letter.includes('A')) {
    // /[BCDF]/는 정규식. 전체에서(g) B,C,D,F를 찾는 것
    return letter.replace(/[BCDF]/g, 'A');
  } else if (letter.includes('B')) {
    return letter.replace(/[CDF]/g, 'B');
  } else if (letter.includes('C')) {
    return letter.replace(/[DF]/g, 'C');
  } else {
    return 'A'.repeat(letter.length);
  }
}

console.log(change(input));