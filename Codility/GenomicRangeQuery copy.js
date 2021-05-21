// you can write to stdout for debugging purposes, e.g.
// console.log('this is a debug message');

function solution(S, P, Q) {
  const impactFactorsMap = { A: 0, C: 1, G: 2, T: 3 };
  const impactFactors = S.split('').map((char) => {
    return impactFactorsMap[char];
  });
  const impactFactorsCount = new Array(4).fill(0);
  impactFactors.forEach((factor) => impactFactorsCount[factor]++);

  /**
   * @params {number[]}
   * @params {number[]}
   * @return {Map[number]: number[]}
   */
  function createImpactFactorsCount(arr, impactFactors) {
    arr.push(0);
    const tempSet = new Set(arr);
    const sortedArr = [...tempSet].sort();
    const factorCountMap = new Map();
    factorCountMap.set(0, [...impactFactorsCount]);

    for (let i = 1; i < sortedArr.length; i++) {
      const prevPosition = sortedArr[i - 1];
      const position = sortedArr[i];
      const tempFactorCount = [...factorCountMap.get(prevPosition)];
      for (let p = prevPosition; p < position; p++) {
        tempFactorCount[impactFactors[p]]--;
      }
      factorCountMap.set(position, tempFactorCount);
    }

    return factorCountMap;
  }

  const impactFactorsCountP = createImpactFactorsCount([...P], impactFactors);
  const impactFactorsCountQ = createImpactFactorsCount([...Q], impactFactors);
  impactFactorsCountQ.forEach((value, key) => value[impactFactors[key]]--);

  const M = P.length;
  const result = new Array(M).fill(0).map((_, index) => {
    const currfactorCountP = impactFactorsCountP.get(P[index]);
    const currfactorCountQ = impactFactorsCountQ.get(Q[index]);
    let i = 0;
    for (i; i < 4; i++) {
      if (currfactorCountP[i] - currfactorCountQ[i] > 0) break;
    }
    return i + 1;
  });

  return result;
}
