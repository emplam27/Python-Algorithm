/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  if (nums.length <= 3) return Math.max(...nums);

  function findRob(houses) {
    DP = Array.from({ length: houses.length }, () => 0);
    DP[0] = houses[0];
    DP[1] = Math.max(houses[0], houses[1]);
    DP[2] = Math.max(houses[0] + houses[2], houses[1]);
    for (let i = 3; i < houses.length; i++) {
      DP[i] = Math.max(DP[i - 2], DP[i - 3]) + houses[i];
    }
    return Math.max(...DP);
  }

  return Math.max(
    findRob(nums.slice(0, nums.length - 1)),
    findRob(nums.slice(1, nums.length))
  );
};
