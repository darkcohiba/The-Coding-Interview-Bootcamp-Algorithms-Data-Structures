function missingNumber(nums) {
    const n = nums.length;
    const expectedSum = n * (n + 1) / 2;
    const actualSum = nums.reduce((acc, num) => acc + num, 0);
    return expectedSum - actualSum;
}

// Test cases
console.log(missingNumber([3,0,1]));  // Output: 2
console.log(missingNumber([0,1]));    // Output: 2
console.log(missingNumber([9,6,4,2,3,5,7,0,1]));  // Output: 8
