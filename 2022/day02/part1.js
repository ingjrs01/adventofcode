const fs = require("fs");
const data = fs.readFileSync('./input.txt',{encoding:'utf8'});

console.log("empezando");
let tmp = data.trim().split("\n").map(line => line.split(" "))

console.log(tmp);

const part1 = (tmp) => {
  let total = 0;
  tmp.forEach(l => {
    if (l[0] === 'A') {
      total += (l[1] === 'X')?4:0;
      total += (l[1] === 'Y')?8:0;
      total += (l[1] === 'Z')?3:0;
    }
    if (l[0] === 'B') {
      total += (l[1] === 'X')?1:0;
      total += (l[1] === 'Y')?5:0;
      total += (l[1] === 'Z')?9:0;
    }
    if (l[0] === 'C') {
      total += (l[1] === 'X')?7:0;
      total += (l[1] === 'Y')?2:0;
      total += (l[1] === 'Z')?6:0;
    }  
  });

  console.log(total);
}

const part2 = (tmp) => {
  let total = 0;
  tmp.forEach(l => {
    if (l[0] === 'A') {
      total += (l[1] === 'X')?3:0;
      total += (l[1] === 'Y')?4:0;
      total += (l[1] === 'Z')?8:0;
    }
    if (l[0] === 'B') {
      total += (l[1] === 'X')?1:0;
      total += (l[1] === 'Y')?5:0;
      total += (l[1] === 'Z')?9:0;
    }
    if (l[0] === 'C') {
      total += (l[1] === 'X')?2:0;
      total += (l[1] === 'Y')?6:0;
      total += (l[1] === 'Z')?7:0;
    }  
  });

  console.log(total);
}


part1(tmp);
part2(tmp);


