/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function (nums) {
  let curr = 0;
  for (let i = 0; i < nums.length; i++) {
    if (i > curr) {
      return false;
    }
    curr = Math.max(nums[i] + i, curr);
  }
  return true;
};
