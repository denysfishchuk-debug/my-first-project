function calc(x, y) {
  return x + y;
}


const c = calc(1, 2);
console.log("const c: " + calc(1, 2));
console.log("Result: " + calc(1, 2));


console.log("1Result: " + calc(1));
console.log("1 2 4 Result: " + calc(1, 2, 4));
console.log("1, asdasdasdasd Result: " + calc(1, "asdasdasdasd"));

//-------------------------

function toUpperCaseClassic(x) {
  return x.toUpperCase();
}

console.log(toUpperCaseClassic("hello")); 


const toUpperCaseArrow = (str) => str.toUpperCase();

console.log(toUpperCaseArrow("Markus")); 

//------------------------------


const names = ["dci", "ubunru", "js"];
const upperNames = names.map(name => name.toUpperCase());

console.log(upperNames); 


