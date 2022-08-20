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

f = new Node('F');
b = new Node('B');
g = new Node('G');
f.left = b;
f.right = g;
a = new Node('A');
d = new Node('D');
h = new Node('H');
b.left = a;
b.right = d;
g.right = h;
c = new Node('C');
e = new Node('E');
d.left = c;
d.right = e;


const tree = new Tree(f);

// p1 = tree.inOrderTrav();
// console.log(p1);

// p2 = tree.preOrderTrav();
// console.log(p2);

const tree2 = new Tree();
tree2.makeTree(['A', 'B', 'C', '', '', 'D', 'E', '', '', 'F', '', '', 'G', '', 'H', '', '']);

p3 = tree2.preOrderTrav();
console.log(p3);
