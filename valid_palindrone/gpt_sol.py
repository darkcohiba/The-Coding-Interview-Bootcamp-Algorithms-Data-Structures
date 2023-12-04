def is_palindrome(s):
    # Convert the string to lowercase and remove non-alphanumeric characters
    clean_string = "".join(char.lower() for char in s if char.isalnum())

    # Check if the cleaned string is a palindrome
    return clean_string == clean_string[::-1]

# Test the function
print(is_palindrome("A man, a plan, a canal: Panama")) # True
print(is_palindrome("race a car")) # False
print(is_palindrome(" ")) # True