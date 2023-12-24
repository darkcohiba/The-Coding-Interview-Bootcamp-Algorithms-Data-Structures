function minimumBribes(q) {
    let bribes = 0;
    const n = q.length;
    for (let i = n - 1; i >= 0; i--) {
        if (q[i] - (i + 1) > 2) {
            console.log("Too chaotic");
            return;
        }

        // Count the number of bribes
        for (let j = Math.max(0, q[i] - 2); j < i; j++) {
            if (q[j] > q[i]) {
                bribes++;
            }
        }
    }

    console.log(bribes);
}

// Example usage
minimumBribes([1, 2, 5, 3, 7, 8, 6, 4]);  // Normal case
minimumBribes([4, 1, 2, 3]);              // Too chaotic case
