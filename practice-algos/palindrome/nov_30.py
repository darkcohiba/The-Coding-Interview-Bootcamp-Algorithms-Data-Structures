# Given an integer x, return true if x is a palindrome, and false otherwise.

def palTest(num):
    revNum = str(num)[::-1]
    return False if "-" in revNum else int(revNum) == num

print(palTest(21))

