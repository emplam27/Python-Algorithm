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
var isBalanced = function (root) {
  let result = true;

  function checkTreeHeight(tree) {
    if (tree === null) return 0;
    const leftHeight = checkTreeHeight(tree.left);
    const rightHeight = checkTreeHeight(tree.right);
    if (Math.abs(leftHeight - rightHeight) > 1) result = false;
    return Math.max(leftHeight, rightHeight) + 1;
  }

  checkTreeHeight(root);
  return result;
};
