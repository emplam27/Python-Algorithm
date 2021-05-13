/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function (num) {
  let left = 1;
  let right = num;
  let mid;
  while (left <= right) {
    // 단항 비트 논리부정 연산자 (Double Bitwise NOT)
    mid = ~~((left + right) / 2);
    // mid = Math.floor((left + right) / 2);
    if (mid ** 2 < num) {
      left = mid + 1;
    } else if (mid ** 2 > num) {
      right = mid - 1;
    } else {
      return true;
    }
  }
  return false;
};
