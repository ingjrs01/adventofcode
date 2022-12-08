const fs = require("fs");
const data = fs.readFileSync('./input.txt',{encoding:'utf8'}).trim().split("\n").map(l => l.split(",").map((p,q)=> p.split("-").map(Number)));

const part1 = datos => {
  let res = datos.map(line=>{
    let inc = 0;
    if (line[0][0] <= line[1][0] && line[0][1] >= line[1][1]) inc = 1; // second contents in firts
    if (line[1][0] <= line[0][0] && line[1][1] >= line[0][1]) inc = 1; // first content in second
    return inc;
  });
  console.log(res.reduce( (a,b)=> a+b,0));
}

const part2 = datos => {
  let res = datos.map(line=>{
    let inc = 0;
    if (line[0][0] <= line[1][0] && line[0][1] >= line[1][0]) inc = 1;
    if (line[0][1] >= line[1][1] && line[1][1] >= line[0][0]) inc = 1;
    if (line[0][0] >= line[1][0] && line[0][0] <= line[1][1]) inc = 1;
    if (line[0][0] >= line[1][0] && line[0][0] <= line[1][1]) inc = 1;
    return inc;
  });
  console.log(res.reduce( (a,b)=> a+b,0));
}

part1(data);
part2(data);
