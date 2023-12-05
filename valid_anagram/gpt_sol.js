function isAnagram(s, t) {
    // If lengths differ, they cannot be anagrams
    if (s.length !== t.length) {
        return false;
    }

    // Function to count characters in a string
    const countCharacters = (str) => {
        const count = {};
        for (let char of str) {
            count[char] = (count[char] || 0) + 1;
        }
        return count;
    };

    // Count characters in both strings
    const sCount = countCharacters(s);
    const tCount = countCharacters(t);

    // Compare character counts
    for (let char in sCount) {
        if (sCount[char] !== tCount[char]) {
            return false;
        }
    }

    return true;
}

console.log(isAnagram('anagram', 'nagaram')); // true
console.log(isAnagram('rat', 'car')); // false
