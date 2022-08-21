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

    inOrderTrav = function() {
        if (!this.root) return [];
        
        const path = [];

        const inOrderTravHelper = (node) => {
            if (!node) return;
            inOrderTravHelper(node.left);
            path.push(node.val);
            inOrderTravHelper(node.right);
        }
        
        inOrderTravHelper(this.root);

        return path;
    }

    preOrderTrav = function() {
        if (!this.root) return [];

        const path = [];

        const preOrderTravHelper = (node) => {
            if (!node) return;
            path.push(node.val);
            preOrderTravHelper(node.left);
            preOrderTravHelper(node.right);
        }

        preOrderTravHelper(this.root);
        return path;
    }

    /**
    * Use preorder array to create tree
    * @param {Array} nodes The values to become nodes in the tree
    */
    makeTree = function(nodes) {
        let nodeIndex = 0;

        const makeTreeHelper = () => {
            let node_val = nodes[nodeIndex];
            if (node_val === "") return;
            const node = new Node(node_val);
            nodeIndex++;
            node.left = makeTreeHelper();
            nodeIndex++;
            node.right = makeTreeHelper();
            return node
        }

        this.root = makeTreeHelper()
    }
}

export { Tree }; 