def isAnagram(s, t) -> bool:
    letter_map = {}
    for index, char in enumerate(s):
        letter_map[char] = index
        

