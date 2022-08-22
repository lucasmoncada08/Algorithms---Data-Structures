

export const visibleTreeNode = (root) => {
    
    if (!root) return 0;

    let numVisible = 1;

    const dfsVisible = (node, maxValue) => {
        if (!node) return;

        if (node.val > maxValue) {
            numVisible++;
            maxValue = node.val;
        }

        dfsVisible(node.left, maxValue);

        dfsVisible(node.right, maxValue);
   
    }

    dfsVisible(root, root.val);

    return numVisible;
}

export const visibleTreeNode2 = (root, maxSoFar=-Infinity) => {

    if (!root) return 0;
    
    let total = 0;

    if (root.val > maxSoFar) {
        total++;
        maxSoFar = root.val;
    }

    total += visibleTreeNode2(root.left, maxSoFar);
    total += visibleTreeNode2(root.right, maxSoFar);

    return total
}


/*
      
  - 3     - 6
      - 8
5 
  - 8
      
*/