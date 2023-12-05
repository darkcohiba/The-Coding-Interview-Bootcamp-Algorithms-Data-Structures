function isPalindrome(s) {
    // Convert the string to lowercase and remove non-alphanumeric characters
    let cleanString = s.toLowerCase().replace(/[^a-z0-9]/g, "");

    // Check if the cleaned string is a palindrome
    let left = 0;
    let right = cleanString.length - 1;
    while (left < right) {
        if (cleanString[left] !== cleanString[right]) {
            return false;
        }
        left++;
        right--;
    }

    // If the loop completes without returning false, it's a palindrome
    return true;
}

// Test the function
console.log(isPalindrome("A man, a plan, a canal: Panama")); // true
console.log(isPalindrome("race a car")); // false
console.log(isPalindrome(" ")); // true