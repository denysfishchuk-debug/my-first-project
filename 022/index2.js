let globalVar = "global Var";

function localScope() {

  let localVar = "local Var";

  console.log("inside:");
  console.log("globalVar:", globalVar); 
  console.log("localVar:", localVar);   
}

localScope();

console.log("outside:");
console.log("globalVar:", globalVar);   // ok
console.log("localVar:", typeof localVar); //undefined

//-------------------------------------

function testFunctionScope() {
  var a = "var inside";
  let b = "let inside";
  const c = "const inside";

  console.log(a); 
  console.log(b); 
  console.log(c); 
}

testFunctionScope();

// console.log(a); //  a is not defined
// console.log(b); //  b is not defined
// console.log(c); //  c is not defined






if (true) {
  var x = "var inside";
  let y = "let insid";
  const z = "const insid";

  console.log("insid: ", x, y, z);
}

console.log("outside:");
console.log("x:", x); // ok
// console.log("y:", y); // y is not defined
// console.log("z:", z); // z is not defined


//-----------------------
console.log("for----------");
for (var i = 0; i < 3; i++) {
  var loopVar = "var inside";
  let loopLet = "let inside";
}

console.log("loopVar:", loopVar); // ok
// console.log("loopLet:", loopLet); // loopLet is not defined

