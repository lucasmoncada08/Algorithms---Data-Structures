/**
 * Function for finding the Max Depth of a Tree using DFS
 * Time Complexity: O(N)
 * Space Complexity: O(d), where d is the max depth
 * @param {Node} node the root node to be searched through
 */

export const maxDepthOfTree = (node) => {

    if (!node) return 0

    const leftDepth = maxDepthOfTree(node.left) + 1;
    const rightDepth = maxDepthOfTree(node.right) + 1;

    return Math.max(leftDepth, rightDepth);

};

