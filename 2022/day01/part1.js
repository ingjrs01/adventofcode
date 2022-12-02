
const fs = require("fs");

const data = fs.readFileSync('./input.txt',{encoding:'utf8'});

const elfos = data.trim().split("\n\n");
const lala = elfos.map(elfo => elfo.split("\n").map(c=> parseInt(c)))
const lele = lala.map(l => l.reduce((a,b)=> a+b,0));

//console.log(elfos);
console.log(lala);
console.log(lele);
const maximo = Math.max(...lele);
console.log(maximo);

let ordenado = lele.sort().reverse().slice(0,3)
console.log(ordenado);
