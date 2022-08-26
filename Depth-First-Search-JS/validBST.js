
const isValidBST = (root) => {

    const isValidBSTHelper = (node, min, max) => {
        if (!node) return true;
        if (node.val < min || node.val > max) return false;

        return isValidBSTHelper(node.left, min, node.val) && isValidBSTHelper(node.right, node.val, max);
    }

    return isValidBSTHelper(root, -Infinity, Infinity);

}

export { isValidBST };