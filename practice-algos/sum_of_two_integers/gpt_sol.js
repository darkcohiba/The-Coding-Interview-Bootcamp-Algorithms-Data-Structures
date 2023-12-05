function getSum(a, b) {
    let carry;
    while ((a & b) !== 0) {
        carry = (a & b) << 1;
        a = a ^ b;
        b = carry;
    }
    return a ^ b;
}

// Test cases
console.log(getSum(1, 2)); // 3
console.log(getSum(2, 3)); // 5
