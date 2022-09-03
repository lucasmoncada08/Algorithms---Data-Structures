/**
 * Get fibonacci number with memoization
 * @param {Number} num fibonacci number to compute
 * @return {Number} computed fibonacci value
 */
const getFibonacciNumber = (num) => {
    const memo = new Map();
    memo.set(0, 0);
    memo.set(1, 1);

    const getFibonacciNumberHelper = (num) => {
        const alreadyComputed = memo.get(num);
        if (alreadyComputed !== undefined) return alreadyComputed;
        const fibRes = getFibonacciNumberHelper(num-1) + getFibonacciNumberHelper(num-2);
        memo.set(num, fibRes);
        return fibRes;
    }
    
    return getFibonacciNumberHelper(num);
}

export { getFibonacciNumber };