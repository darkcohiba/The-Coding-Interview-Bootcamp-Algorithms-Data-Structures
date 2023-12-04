def isPalindrome(s: str) -> bool:
    lower_string = s.lower()
    for index, char in enumerate(lower_string):
        if char != lower_string[-index -1]:
            return False
    return True
# steps
# Normalize the String:

# Convert the entire string to lowercase.
# Remove all characters that are not letters or numbers.
# Check for Palindrome:

# Compare characters from the start and the end of the string, moving towards the center.
# If all corresponding characters match, it's a palindrome.
# If any do not match, it's not a palindrome.
# Return the Result:

# Your function should return true if the string is a palindrome, and false otherwise.


print(isPalindrome("a man I nam a"))
print(isPalindrome("ili"))
print(isPalindrome("a man I nam"))
print(isPalindrome("a man 'I' nam a"))