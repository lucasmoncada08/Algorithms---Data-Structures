import { expect } from 'chai';
import { Tree } from '../Depth-First-Search-JS/Tree.js';
import { maxDepthOfTree } from '../Depth-First-Search-JS/maxDepthOfTree.js'

describe("Depth First Search Methods", () => {

    let tree1 = new Tree();
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

    it("returns back a found node if available in tree", () => {
        expect(tree1.depthFirstSearch(tree1.root, 'A')?.val).to.equal('A');
        expect(tree1.depthFirstSearch(tree1.root, 'G')?.val).to.equal('G');
        expect(tree1.depthFirstSearch(tree1.root, 'Z')?.val).to.equal(undefined);
    });
});

describe("Max Depth of Tree", () => {
    let tree1 = new Tree();
    tree1.makeTree(['A', 'B', 'C', '', '', 'D', 'E', '', '', 'F', '', '', 'G', '', 'H', '', '']);
    
    let tree2 = new Tree();
    tree2.makeTree([1, 2, 3, 4, 5, 6, '', '', '', '', '', '', '',])

    let tree3 = new Tree();
    tree3.makeTree([1, '', ''])

    let tree4 = new Tree();
    tree4.makeTree([])


    it("returns the maximum depth of a tree", () => {
        expect(maxDepthOfTree(tree1.root)).to.equal(4);
        expect(maxDepthOfTree(tree2.root)).to.equal(6);
        expect(maxDepthOfTree(tree3.root)).to.equal(1);
        expect(maxDepthOfTree(tree4.root)).to.equal(0);
    });
})