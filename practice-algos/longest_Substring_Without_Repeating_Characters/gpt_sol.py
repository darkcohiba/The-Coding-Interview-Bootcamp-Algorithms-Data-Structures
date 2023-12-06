def length_of_longest_substring(s):
    char_set = set()
    left = maxLength = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        maxLength = max(maxLength, right - left + 1)

    return maxLength
