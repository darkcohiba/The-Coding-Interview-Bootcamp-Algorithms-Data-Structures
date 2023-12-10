# Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


# Solution Guide

To explain the steps for solving the "Product of Array Except Self" problem, we'll break it down into a series of straightforward steps in pseudocode. The goal is to construct an output array where each element at index i is equal to the product of all the elements in the input array except the one at i, without using division and achieving this in O(n) time complexity.

###  Explanation:
1. Initialize Arrays: Create three arrays: left, right, and answer. left and right will temporarily store the products of elements to the left and right of each index, respectively.

2. Fill the Left Array: Traverse nums from left to right. Each element in left stores the product of all elements to the left of the current index in nums.

3. Fill the Right Array: Traverse nums from right to left. Each element in right stores the product of all elements to the right of the current index in nums.

4. Construct the Answer Array: The final answer for each index is the product of the values in the left and right arrays at that index, effectively multiplying all elements except the one at the current index in nums.

5. Return the Result: The answer array contains the required product for each index, as per the problem statement.

This approach ensures that the result for each index is calculated without using division and in linear time complexity.