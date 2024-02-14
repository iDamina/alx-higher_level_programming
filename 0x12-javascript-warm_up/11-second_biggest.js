#!/usr/bin/node

const args = process.argv.slice(2);
const numArgs = args.length;

// Use console.log(...) to print the output
if (numArgs === 0 || numArgs === 1) {
  console.log('0');
} else {
  // Convert arguments to integers
  const integers = args.map(arg => parseInt(arg));

  // Sort the integers in descending order
  const sortedIntegers = integers.sort((a, b) => b - a);

  // Find the second biggest integer
  const secondBiggest = sortedIntegers[1];

  console.log(secondBiggest);
}
