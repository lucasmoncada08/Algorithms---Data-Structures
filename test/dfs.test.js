import { expect } from 'chai';
import { Tree } from '../Depth-First-Search-JS/Tree.js';

describe("Depth First Search Methods", () => {

    let tree1 = new Tree()
    tree1.makeTree(['A', 'B', 'C', '', '', 'D', 'E', '', '', 'F', '', '', 'G', '', 'H', '', '']);

    it("makes a pre-order tree", () => {
        const tree = new Tree();
        tree.makeTree(['A', 'B', 'C', '', '', 'D', 'E', '', '', 'F', '', '', 'G', '', 'H', '', '']);
        const preOrderPath = tree.preOrderTrav();
        expect(preOrderPath).deep.to.equal(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']);
    });

    it("returns a pre-order path of a tree", () => {
        expect(tree1.preOrderTrav()).deep.to.equal(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']);
    });

    it("returns a in-order path of a tree", () => {
        expect(tree1.inOrderTrav()).deep.to.equal(['C', 'B', 'E', 'D', 'F', 'A', 'G', 'H']);
    });

    it("returns a post-order path of a tree", () => {
        expect(tree1.postOrderTrav()).deep.to.equal(['C', 'E', 'F', 'D', 'B', 'H', 'G', 'A']);
    });
});