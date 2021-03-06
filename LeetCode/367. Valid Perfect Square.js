/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function (num) {
  let i = 1;
  while (i < 2 ** 16) {
    if (i ** 2 === num) {
      return true;
    }
    i++;
  }
  return false;
};
