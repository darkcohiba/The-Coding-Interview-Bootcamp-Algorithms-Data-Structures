def lengthOfLongestSubstring(s: str) -> int:
    charSet= set()
    l = 0
    result = 0
    for r in range(len(s)):
        # print(s[r])
        while s[r] in charSet:
            # print("increasing l")
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        # print(result, r, l)
        result = max(result, r - l + 1)
        # print(result, r, l, 'after')

    return result






print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
