const fs = require('fs');

let input = fs.readFileSync(0,'utf8').toString().split("\n")
let answer = ''

for(let i = 1; i <= input[0]; i++) {
    line = input[i].split(' ')
    answer += parseInt(line[0]) + parseInt(line[1]) + "\n"
}

console.log(answer)