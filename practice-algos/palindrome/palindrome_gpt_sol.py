def isPalindrome(x):
    # Convert the integer to a string
    str_x = str(x)
    
    # Compare characters from both ends
    for i in range(len(str_x) // 2):
        if str_x[i] != str_x[-i-1]:
            return False
    return True

# Example usage
print(isPalindrome(121))  # Output: True
print(isPalindrome(-121)) # Output: False
print(isPalindrome(10))   # Output: False