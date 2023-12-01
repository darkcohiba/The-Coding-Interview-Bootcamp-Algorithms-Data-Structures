from icecream import ic
def isValid(s):
    bracket_map = {')': '(', '}': '{', ']': '['}
    opening_brackets = {'(', '{', '['}
    stack = []
    # iterate through all of our characts
    for char in s:
        # if a character is an opening bracket of any type we will add it to our stack
        if char in opening_brackets:
            ic(char, " is an opening")
            stack.append(char)
        else:
        # if the character is not an opening bracket of any type we will check to see if we have any opening brackets in our stack list, if we do not we return false here
            if not stack:
                ic("no stack")
                return False
            # if we do have stuff in our stack array, we want to pull the last element in the array and match it up the corresponding bracket in our bracket map. If the element does not equal the corresponding bracket we will return false
            else:
                ic(bracket_map[char])
                ic(char)
                ic(stack[-1])
                if stack.pop() != bracket_map[char]:
                    print('stack.pop does not equal bracketmap')
                    return False
    # if we get here then we we have sucessfully removed everything from our stack we will return the empty stack, which would be false but it will return as true since we have sucessfully removed all the matches
    return not stack


print(isValid("((())))"))     