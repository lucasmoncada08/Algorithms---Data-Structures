/**
 * Given string, return distinct permutations.
 * Time Complexity: O(N!); Space Complexity: O(N!)
 * @param {String} string string to find permuations of
 * @return {Array<String>} list of permutations
 */
const findStringPermutations = (string) => {
    
    const permutations = [];
    const letters = [...string];

    const findPermutationsHelper = (perm, options) => {

        if (perm.length === letters.length) {
            permutations.push(perm.join(''));
            return;
        }

        for (let i=0; i<letters.length; i++) {
            if (options[i]) continue;
            perm.push(letters[i]);
            options[i] = true;
            findPermutationsHelper(perm, options);
            perm.pop();
            options[i] = false;
        }
    }
    findPermutationsHelper([], new Array(letters.length).fill(false));
    return permutations;

}

export { findStringPermutations };
