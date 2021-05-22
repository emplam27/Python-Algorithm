// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(A) {
  let minAvg = (A[0] + A[1]) / 2;
  let startPosition = 0;

  for (let i = 2; i < A.length; i++) {
    const threeAvg = (A[i - 2] + A[i - 1] + A[i]) / 3;
    if (threeAvg < minAvg) {
      minAvg = threeAvg;
      startPosition = i - 2;
    }

    const twoAvg = (A[i - 1] + A[i]) / 2;
    if (twoAvg < minAvg) {
      minAvg = twoAvg;
      startPosition = i - 1;
    }
  }

  return startPosition;
}
