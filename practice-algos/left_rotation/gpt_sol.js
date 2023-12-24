function leftRotate(arr, d) {
    let n = arr.length;
    d %= n;  // This line handles cases where d > n
    return arr.slice(d).concat(arr.slice(0, d));
}

// Example usage
let arr = [1, 2, 3, 4, 5];
let d = 2;
let result = leftRotate(arr, d);
console.log("Rotated Array:", result);