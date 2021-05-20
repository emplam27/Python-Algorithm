function solution(K, M, A) {
  /**
   * @param {number} block수를 구하고자 하는 largeSum
   * @return {number} block의 수 반환
   */
  function getBlocksWithinLargeSum(largeSum) {
    let blocks = 1;
    let tempSum = 0;

    for (let i = 0; i < A.length; i++) {
      if (tempSum + A[i] > largeSum) {
        blocks += 1;
        tempSum = A[i];
      } else {
        tempSum += A[i];
      }
    }

    return blocks;
  }

  let maxValue = A.reduce((a, b) => a + b, 0);
  let minValue = A.reduce((a, b) => Math.max(a, b), 0);

  while (minValue < maxValue) {
    const midValue = parseInt((minValue + maxValue) / 2);
    const blocks = getBlocksWithinLargeSum(midValue);
    if (blocks > K) {
      minValue = midValue + 1;
    } else {
      maxValue = midValue;
    }
  }

  return maxValue;
}
