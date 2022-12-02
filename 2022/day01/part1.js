const fs = require("fs");
const data = fs.readFileSync('./input.txt',{encoding:'utf8'});
const elfos = data.trim().split("\n\n");
const lala = elfos.map(elfo => elfo.split("\n").map(c=> parseInt(c)))
const lele = lala.map(l => l.reduce((a,b)=> a+b,0));
console.log(Math.max(...lele));
console.log(maximo);
console.log (lele.sort((a,b)=>{return a-b}).reverse().slice(0,3).reduce((a,b)=> a+b,0))
