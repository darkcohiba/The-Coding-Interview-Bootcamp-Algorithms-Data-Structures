function jumpingOnClouds(c) {
    let n = c.length;
    let jumps = 0;
    let i = 0;

    while (i < n - 1) {
        // Check if a jump of 2 is possible, otherwise jump by 1
        if (i + 2 < n && c[i + 2] === 0) {
            i += 2;
        } else {
            i++;
        }
        jumps++;
    }

    return jumps;
}

// Example usage
let clouds = [0, 1, 0, 0, 0, 1, 0];
console.log("Minimum jumps:", jumpingOnClouds(clouds));
