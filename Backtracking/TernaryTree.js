class Node {
    constructor(val, children=[]) {
        this.val = val;
        this.children = children;
    }
}

class TernaryTree {
    constructor() {
        this.root = null;
    }

    makeTernaryTree(nodes, index=[0]) {
        
        const node = new Node(nodes[index[0]]);
        index[0]++;
        while (nodes[index[0]] !== "" && index < nodes.length) {
            node.children.push(this.makeTernaryTree(nodes, index));
        }
        index[0]++;

        return node;
    }
}

export { TernaryTree };

const tree1 = new TernaryTree();
tree1.root = tree1.makeTernaryTree([1, 2, "", 3, 4, "", 5, "", "", ""])