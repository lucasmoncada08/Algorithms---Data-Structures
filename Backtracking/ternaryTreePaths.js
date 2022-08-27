/**
 * Find all root-to-leaf paths. Time Complexity: O(N); Space Complexity: O(N)
 * @param {Node} root root of tree
 * @return {Array} root-to-leaf paths
 */
const ternaryTreePaths = (root) => {
    if (!root) return [];

    const paths = [];

    const handleNode = (node, currentPath) => {
        if (!node.children.length) paths.push(currentPath);

        node.children.forEach((child) => handleNode(child, currentPath+`->${child.val}`))
    }

    handleNode(root, `${root.val}`);
    return paths;
}

export { ternaryTreePaths };