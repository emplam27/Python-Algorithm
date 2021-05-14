/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  nums.forEach((value, index) => {
    if (nums[index - 1] > 0) {
      nums[index] = value + nums[index - 1];
    }
  });

  return Math.max(...nums);
};
