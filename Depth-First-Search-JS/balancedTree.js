/**
 * Find if the given tree is balanced or not
 * Time Complexity: O(N)
 * Space Complexity: O(d), where d is depth
 * @param {Node} root root of tree to check
 * @return {Boolean} if the tree is balanced
 */

const isBalancedTree = (root) => {
    if (!root) return false;

    const isBalancedHelper = (node) => {
        if (!node) return 0;

        const left = isBalancedHelper(node.left);
        if (left === false) return false;

        const right = isBalancedHelper(node.right);
        if (right === false) return false;

        if (Math.abs(left - right) > 1) return false;
        
        return Math.max(left, right) + 1;
    }

    return isBalancedHelper(root) !== false;
    
}

export { isBalancedTree };
