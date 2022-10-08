#!/usr/bin/node
exports.esrever = function (list) {
  let temp;
  const size = list.length;
  for (let i = 0; i < size / 2; i++) {
    temp = list[i];
    list[i] = list[size - i - 1];
    list[size - i - 1] = temp;
  }
  return (list);
};
