/**
 * @param {number[][]} graph
 * @return {boolean}
 */
var isBipartite = function (graph) {
  function checkNodesWithDFS(currNode, isRedNode) {
    for (let i = 0; i < graph[currNode].length; i++) {
      const nextNode = graph[currNode][i];
      if (isRedNode && redNodes.has(nextNode)) return false;
      if (isRedNode && !blueNodes.has(nextNode)) {
        blueNodes.add(nextNode);
        if (!checkNodesWithDFS(nextNode, !isRedNode)) return false;
      }
      if (!isRedNode && blueNodes.has(nextNode)) return false;
      if (!isRedNode && !redNodes.has(nextNode)) {
        redNodes.add(nextNode);
        if (!checkNodesWithDFS(nextNode, !isRedNode)) return false;
      }
    }
    return true;
  }

  const redNodes = new Set();
  const blueNodes = new Set();
  for (let node = 0; node < graph.length; node++) {
    if (graph[node].length > 0 && !redNodes.has(node) && !blueNodes.has(node)) {
      redNodes.add(node);
      if (!checkNodesWithDFS(node, true)) return false;
    }
  }
  return true;
};
