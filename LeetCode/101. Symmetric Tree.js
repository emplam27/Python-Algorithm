/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function (root) {
  const queue = [];
  queue.push([root.left, root.right]);
  while (queue.length > 0) {
    const [leftTree, rightTree] = queue.pop();
    // 아직 깊이가 2 이상인 트리
    if (leftTree && rightTree) {
      // 두 트리의 루트값이 다르면 실패, 같으면 queue에 짝 맞춰서 삽입
      if (leftTree.val !== rightTree.val) return false;
      queue.push([leftTree.left, rightTree.right]);
      queue.push([leftTree.right, rightTree.left]);
      continue;
    }
    // 리프노드 비교
    if (leftTree !== null || rightTree !== null) return false;
  }
  return true;
};
