# PROBLEM STATEMENT

You are given an integer array nums of length n, and an integer array queries of length m.

Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

# EXAMPLE

    Input: nums = [4,5,2,1], queries = [3,10,21]
    Output: [2,3,4]
    Explanation: We answer the queries as follows:
    - The subsequence [2,1] has a sum less than or equal to 3. It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
    - The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
    - The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.

# APPROACH

We have to find a "Subsequence" not a "Subarray". So we can pick any elements in sequence.

So, we can find prefix sum array of given array such that each poisiton indicates the sum till that point. And in this way, all we need to search is a sum that is <= targetSum. We can do that by sorting the second array first before finding its prefix sum array.

As we are asked for the longest subsequency, it means even if the sum we get at mid is <= target, we won't stop searching.

