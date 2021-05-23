// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(S, P, Q) {
  const SLen = S.length;
  const impactFactorsMap = { A: 0, C: 1, G: 2, T: 3 };
  const arr = Array.from(Array(4), () => Array(SLen).fill(0));
  S.split('').forEach((char, index) => {
    arr[impactFactorsMap[char]][index]++;
  });
  for (let factor = 0; factor < 4; factor++) {
    for (let index = 1; index < SLen; index++) {
      arr[factor][index] += arr[factor][index - 1];
    }
  }

  const resultLen = P.length;
  const result = Array(resultLen).fill(0);
  for (let i = 0; i < resultLen; i++) {
    for (let factor = 0; factor < 4; factor++) {
      if (P[i] === Q[i]) {
        result[i] = impactFactorsMap[S[P[i]]] + 1;
        break;
      }

      const DiffP = arr[factor][P[i]];
      const DiffQ = arr[factor][Q[i]];
      if (DiffQ - DiffP > 0) {
        result[i] = factor + 1;
        break;
      }
    }
  }

  return result;
}
