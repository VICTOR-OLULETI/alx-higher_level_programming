#!/usr/bin/node
exports.converter = function (base) {
  return function (item) {
    return (item.toString(base));
  };
};
