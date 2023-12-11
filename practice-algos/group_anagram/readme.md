# Group Anagram

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.


# Guide to Solving the Problem
1. Understanding the Problem: Recognize that anagrams, when sorted, become the same string. This characteristic can be used to group them.

2. Choosing a Data Structure: Use a hash table to efficiently group anagrams. The sorted version of each string serves as a unique key.

3. Sorting Each String: For each string in the input array, sort its characters. This can be done using the built-in sort function in both Python and JavaScript.

4. Grouping the Anagrams: Use the sorted string as a key in the hash table and append the original string to the list (or array) at this key.

5. Returning the Result: Since the hash table now groups all anagrams together, return its values, which are the required groups.

6. Edge Cases: Consider edge cases such as empty strings or single-character strings. The algorithm works seamlessly for these cases as well.

This approach ensures that each group of anagrams is collected together, and it does so efficiently, with the primary operation being sorting of individual strings. The overall time complexity mainly depends on the sorting algorithm, typically O(n * k log k), where n is the number of strings and k is the maximum length of a string in the array.