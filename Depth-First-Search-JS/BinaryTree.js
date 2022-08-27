import { Node } from './Tree.js'

class BinaryTree {
    constructor() {
        this.root = null;
    }

    insert = function(value) {
        if (!this.root) {
            this.root = new Node(value);
            return;
        }

        const findNext = (node, value) => {
            if (node.val === value) return;
            else if (node.val > value) {
                if (!node.left) {
                    node.left = new Node(value);
                    return;
                }
                findNext(node.left, value);
            }
            else {
                if (!node.right) {
                    node.right = new Node(value);
                    return;
                }
                findNext(node.right, value);
            }
        }

        findNext(this.root, value);
    }

    search = function(value) {
        if (!this.root) return null;

        const searchHelper = (node, value) => {
            if (!node) return null;
            if (node.val === value) return node;
            if (node.val > value) return searchHelper(node.left, value);
            return searchHelper(node.right, value);
        }

        return searchHelper(this.root, value);
    }
}

export { BinaryTree };