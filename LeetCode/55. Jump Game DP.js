/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function (nums) {
  const DP = Array.from({ length: nums.length }, () => false);
  stack = [];
  stack.push(0);
  DP[0] = true;
  while (stack.length > 0) {
    const position = stack.pop();
    for (let i = 0; i <= nums[position]; i++) {
      if (position + i > nums.length - 1) continue;
      if (position + i === nums.length - 1) return true;
      if (DP[position + i] === false) {
        DP[position + i] = true;
        stack.push(position + i);
      }
    }
  }
  return false;
};
