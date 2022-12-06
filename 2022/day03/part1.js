const fs = require("fs");
const data = fs.readFileSync('./input.txt',{encoding:'utf8'});

var abc = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26,
"A":27,"B":28,"C":29,"D":30,"E":31,"F":32,"G":33,"H":34,"I":35,"J":36,"K":37,"L":38,"M":39,"N":40,"O":41,"P":42,"Q":43,"R":44,"S":45,"T":46,"U":47,"V":48,"W":49,"X":50,"Y":51,"Z":52};

const part1 = datos => {
  let input = datos.trim().split("\n").map(line => {return {left:line.substring(0,line.length/2),right:line.substring(line.length/2 ,line.length)}});
  let lala = input.map(line => {
    let letras = {}
    for (let i=0;i < line.left.length;i++) {
      if (line.right.includes(line.left.charAt(i))) 
        letras[line.left.charAt(i)] = abc[line.left.charAt(i)];
    }
    return Object.values(letras).reduce( (a,b)=> a+b,0)
  });
  console.log(lala.reduce((a,b) => a+b,0));
}

const part2 = datos => {
  let input = datos.trim().split("\n");
  let total = 0;

  for (let i = 0;i < input.length;i += 3) {
    let letras = {};
    //console.log(input.slice(i,i+3));
    for (let j = 0; j < input[i].length;j++) {
      let letter = input[i].charAt(j);       
      if (input[i+1].includes(letter) && input[i+2].includes(letter) ) {
        letras[letter] = abc[letter];
      }
    }
    total += Object.values(letras).reduce((a,b)=> a+b,0);
  }
  console.log(total);
}

part1(data);
part2(data);
