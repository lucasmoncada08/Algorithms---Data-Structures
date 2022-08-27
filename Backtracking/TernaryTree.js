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

    makeTernaryTree(nodes, index=0) {
        
        const node = new Node(nodes[index++]);
        while (nodes[index] !== "" && index < nodes.length) {
            node.children.push(this.makeTernaryTree(nodes, index));
        }
        index++;

        return node;
    }
}