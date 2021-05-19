function solution(H) {
  const stack = [];
  stack.push(H[0]);
  let result = 0;

  for (let i = 1; i < H.length; i++) {
    const curr = H[i];
    if (stack[stack.length - 1] < curr) {
      stack.push(curr);
    } else if (stack[stack.length - 1] > curr) {
      while (stack[stack.length - 1] > curr) {
        stack.pop();
        result++;
      }
      if (stack[stack.length - 1] !== curr) {
        stack.push(curr);
      }
    }
  }

  result += stack.length;
  return result;
}
