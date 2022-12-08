const fs = require("fs");
const [data,ordenes] = fs.readFileSync('./test.txt',{encoding:'utf8'}).trim().split("\n\n");

const part1 = (datos,ordenes) => {
  console.log("Los datos: ");
  console.log(datos);
  console.log("Ordenes: ");
  console.log(ordenes)

}

//const part2 = datos => {
//}


part1(data,ordenes);
//part2(data);
