#!/usr/bin/node
const arr = process.argv;
function findSecondLargest (ar) {
  const args = process.argv.length;
  const array1 = [];
  if (args <= 3) {
    return (0);
  }
  for (let j = 2; j < args; j++) {
    array1.push(parseInt(ar[j], 10));
  }
  const max = Math.max.apply(null, array1);
  array1[array1.indexOf(max)] = -Infinity;
  const max2 = Math.max.apply(null, array1);
  return (max2);
}
console.log(`${findSecondLargest(arr)}`);
