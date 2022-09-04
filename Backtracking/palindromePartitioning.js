/**
 * Returns the possible partitions of a given string where all partitions are palindromes
 * @param {String} string Given string to find palindrome partitions of
 * @returns {Array<String>} array of all palindrome partitions
 */
const palindromePartition = (string) => {
    
    const palindromePartitions = [];

    const palindromePartitionHelper = (index, currentPartition) => {

        currentPartition[currentPartition.length-1] += string[index];
        index++;

        if (isPalindrome(currentPartition[currentPartition.length-1])) {
            if (index === string.length) {
                palindromePartitions.push([...currentPartition]);
                return;
            }
            currentPartition.push("");
            palindromePartitionHelper(index, currentPartition);
            currentPartition.pop();
        };

        if (index === string.length) return;

        palindromePartitionHelper(index, currentPartition);
    };

    palindromePartitionHelper(0, [""]);

    return palindromePartitions;

};

const isPalindrome = (word) => {
    for (let i=0; i<Math.floor(word.length)-1; i++) {
        if (word[i] !== word[word.length-i-1]) return false;
    }

    return true;
};

export { palindromePartition };
