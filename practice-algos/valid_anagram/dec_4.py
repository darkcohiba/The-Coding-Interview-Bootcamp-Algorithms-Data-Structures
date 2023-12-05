def isAnagram(s, t) -> bool:
    if len(s) != len(t):
        return False

    # Create a count map for each character in s
    letter_count = {}
    for char in s:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1

    # Decrement the count for each character in t
    for char in t:
        if char not in letter_count:
            return False

        letter_count[char] -= 1
        if letter_count[char] < 0:
            return False
    return True

print(isAnagram('anagram', 'nagaram'))  # Should return True
print(isAnagram('rat', 'car'))  # Should return False
