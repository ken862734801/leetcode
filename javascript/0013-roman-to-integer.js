/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function (s) {
  const symbols = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };
  let total = 0;
  for (let i = 0; i < s.length; i++) {
    let char = symbols[s[i]];
    if (i + 1 < s.length && char < symbols[s[i + 1]]) {
      total -= char;
    } else {
      total += char;
    }
  }

  return total
};
