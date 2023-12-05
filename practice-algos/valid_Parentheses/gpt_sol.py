def isValid(s):
    # Early return if the string length is odd
    if len(s) % 2 != 0:
        return False

    # Dictionary and set for bracket mapping
    bracket_map = {')': '(', '}': '{', ']': '['}
    opening_brackets = {'(', '{', '['}
    stack = []

    for char in s:
        if char in opening_brackets:
            stack.append(char)
        else:
            # Stack should not be empty when a closing bracket appears
            if not stack:
                return False
            # Check if the popped element is the matching opening bracket
            if stack.pop() != bracket_map[char]:
                return False

    # The stack should be empty if all brackets are matched
    return not stack

# Example usage
print(isValid("()"))      # Output: True
print(isValid("()[]{}"))  # Output: True
print(isValid("(]"))      # Output: False