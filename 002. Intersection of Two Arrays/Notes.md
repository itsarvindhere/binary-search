# PROBLEM STATEMENT

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

# EXAMPLE

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

# APPROACH 1 -> BINARY SEARCH

Intersection means a number if present in both the arrays. So, for each number in first array, we can use binary search to search it in second array. If it is present, then we can add that number to the output array. 

Since we should have a sorted array for Binary Search, that means we first need to sort second array.

Time Complexity -> O(nlogn)
Space Complexity -> O(1)

# APPROACH 2 -> SET

Since all we want to see is if a number that is present in first array is also tehre in second array or not, we can make use of a set. Since we can check if a number is present in set in O(1) time, we can create a set of first array and then for each element in second array, just check if the set contains it or not. If yes, then add it to output array.

Time Complexity -> O(n)
Space Complexity -> O(n)