/*
Tree Structure for basic tree operations such as tree traversals and making a tree
*/

class Node {
    constructor(val, left=null, right=null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Tree {
    constructor(root) {
        this.root = root;
    }

    /**
    * Use preorder array to create tree
    * @param {Array} nodes The values to become nodes in the tree
    */
    makeTree = function(nodes) {
        let nodeIndex = 0;

        if (!nodes.length) return;

        const makeTreeHelper = () => {
            let node_val = nodes[nodeIndex];
            if (node_val === "") return;
            const node = new Node(node_val);
            nodeIndex++;
            node.left = makeTreeHelper();
            nodeIndex++;
            node.right = makeTreeHelper();
            return node;
        }

        this.root = makeTreeHelper();
    }

    // breadthFirstSearch = function(root, target) {
    //     if (!root) return -1;
        
    // }

    /**
     * Depth First Search of a Tree using the root
     * @param {Node} root the starting point
     * @param {any} target the value to search for
     * @returns {Node|undefined} node with target value
     */
    depthFirstSearch = function(root, target) {
        if (!root) return;
        if (root.val == target) return root;

        const left = this.depthFirstSearch(root.left, target);
        if (left) return left;
        const right = this.depthFirstSearch(root.right, target);
        return right;
    }
}

export { Tree, Node }; 