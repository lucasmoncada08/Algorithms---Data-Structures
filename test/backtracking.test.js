import { expect } from 'chai';
import { TernaryTree } from '../Backtracking/TernaryTree.js';
import { ternaryTreePaths } from '../Backtracking/ternaryTreePaths.js';

describe("Test ternary tree paths function", () => {
    const tree1 = new TernaryTree();
    tree1.root = tree1.makeTernaryTree([1, 2, '', 3, 4, '', 5, '', '', '']);

    const tree2 = new TernaryTree();
    tree2.root = tree2.makeTernaryTree([1, 2, 3, 4, '', '', 5, '', '', ''])

    const tree3 = new TernaryTree();

    it("Check tree path functionality", () => {
        expect(ternaryTreePaths(tree1.root)).to.deep.equal(["1->2", "1->3->4", "1->3->5"]);
        expect(ternaryTreePaths(tree2.root)).to.deep.equal(["1->2->3->4", "1->2->5"]);
        expect(ternaryTreePaths(tree3.root)).to.deep.equal([]);
    });
});