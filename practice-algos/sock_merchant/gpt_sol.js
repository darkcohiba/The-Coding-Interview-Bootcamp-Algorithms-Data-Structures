function sockMerchant(n, ar) {
    const colorCounts = {};
    ar.forEach(color => {
        colorCounts[color] = (colorCounts[color] || 0) + 1;
    });

    let pairs = 0;
    Object.values(colorCounts).forEach(count => {
        pairs += Math.floor(count / 2);
    });

    return pairs;
}

// Example usage
const n = 7;
const ar = [1, 2, 1, 2, 3, 1, 2];
console.log(sockMerchant(n, ar));  // Output: 2
