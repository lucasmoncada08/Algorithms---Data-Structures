/**
 * Check if the given word can be created using the options given. Options can be used multiple times.
 * @param {String} word full word to be created
 * @param {Array<String>} options possible words to be used as possible substrings
 * @returns {Boolean} if the word can be created from the options
 */
const wordBreak = (word, options) => {

    const seenWords = new Set();

    const checkWordBreak = (currentWord) => {
        if (currentWord.length > word.length) return false;
        if (seenWords.has(currentWord)) return false;

        if (currentWord === word) return true;

        seenWords.add(currentWord);

        for (const subWord of options) {
            currentWord += subWord;
            if (checkWordBreak(currentWord)) return true;
            currentWord = currentWord.slice(0, currentWord.length - subWord.length); // remove the last subWord
        };

        return false;

    };

    return checkWordBreak("");
};

export { wordBreak };
