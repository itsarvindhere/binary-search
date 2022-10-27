# PROBLEM STATEMENT

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

# BINARY SEARCH APPROACH

Peak element means an element that is bigger than both its neighbours. So that's the condition to check if an element at mid is peak or not.

Since first or last element can be peak as well, in that case, we can take previous or next elements as negative infinity as given in problem statement.