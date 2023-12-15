function countingValleys(steps, path) {
    let seaLevel = 0;
    let valleys = 0;
    let inValley = false;

    for (let step of path) {
        if (step === 'U') {
            seaLevel++;
        } else {
            seaLevel--;
        }

        if (seaLevel < 0 && !inValley) {
            valleys++;
            inValley = true;
        } else if (seaLevel >= 0) {
            inValley = false;
        }
    }

    return valleys;
}

// Example usage
const steps = 8;
const path = "DDUUUUDD";
console.log(countingValleys(steps, path));  // Output: 1
