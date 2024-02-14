#!/usr/bin/node
function add (a, b) {
  const c = a + b;
  console.log(c);
}

const firstNumber = process.argv[2];
const secondNumber = process.argv[3];

add(Number(firstNumber), Number(secondNumber));
