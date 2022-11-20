# PROBLEM STATMENT

A split of an integer array is good if:

   1. The array is split into three non-empty contiguous subarrays - named left, mid, right respectively from left to right.
   2. The sum of the elements in left is less than or equal to the sum of the elements in mid, and the sum of the elements in mid is less than or equal to the sum of the elements in right.

Given nums, an array of non-negative integers, return the number of good ways to split nums. As the number may be too large, return it modulo 109 + 7.

# EXAMPLE

Input: nums = [1,2,2,2,5,0]
Output: 3
Explanation: There are three good ways of splitting nums:
[1] [2] [2,2,5,0]
[1] [2,2] [2,5,0]
[1,2] [2,2] [5,0]


# APPROACH

Since we want to split into three subarrays, what we can try to do is for each possible ending index of right boundary of the "left" subarray, we can try to find what is the leftmost index at which "mid" subarray can end and even then the condition will hold true. Similarly, we can try finding the rightmost index.

In this way, for every possible boundary of "left" subarray, we can find how many ways are there by "rightmostindex - leftmostindex + 1"

For example, in nums = [1,2,2,2,5,0], if the left subarray ends at index 0

Then, the "mid" subarray can either end at index 1 or at index 2. In both cases, the condition will still hold true. Hence, it means, when the left subarray ends at index 0, there are two ways to split the array into three subarrays so that condition is met. And those two ways are ->

            [1] [2] [2,2,5,0]
            [1] [2,2] [2,5,0]
