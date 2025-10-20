console.log('sdasdasd'); 


let letvar = 10;
letvar = 15;
console.log(letvar); // 15


const constvar = 100;
//constvar = 120;  // Assignment to constant variable.


// {
//   let a = 1;
//   const b = 2;
//   console.log(a, b); // 1, 2
// }
// console.log(a); // ReferenceError
// console.log(b); // ReferenceError



let name = "Denys";         // String
let age = 30;               // Number
let isStudent = true;       // Boolean
let empty = null;           // null
let notAssigned;            // undefined

console.log(typeof name);        // "string"
console.log(typeof age);         // "number"
console.log(typeof isStudent);   // "boolean"
console.log(typeof empty);       // "object"
console.log(typeof notAssigned); // "undefined"

console.log("null undefined"); 
let a = null;        
let b;              

console.log(a); 
console.log(b); 

console.log("Strings"); 
let sentence = "DCI ubuntu Linux"; 



console.log(sentence.toUpperCase()); 

console.log(sentence.toLowerCase()); 

console.log(sentence.includes("ubuntu")); 

console.log(sentence.slice(0, 10)); 

console.log(sentence.replace("ubuntu", "Windows")); 


console.log("Num"); 
let x = 12;
let y = 5;

console.log("a + b =", x + y);       
console.log("a - b =", x - y);       
console.log("a * b =", x * y);       
console.log("a / b =", x / y);       
console.log("a % b =", x % y);       
console.log("a ** b =", x ** y);     


let c = 3;
let d = 2;
let result = (x + y) * c / d;
console.log("Complex expression:", result); 

console.log("Logical and Comparison Operators"); 

console.log(5 == "5");   
console.log(5 === "5"); 

let isTrue = true;
let isFalse = false;

console.log(isTrue && isFalse); 
console.log(isTrue || isFalse); 
console.log(!isFalse);  

console.log("Step 3"); 

console.warn("warning!");
console.error("error!");
console.info("info.");

let user = { name: "Denys", age: 100500, student: true };
console.table(user); //cool


//I really liked using `console.table();` — it was a revelation for me.
