# PROBLEM STATEMENT

You are given two strings s and p where p is a subsequence of s. You are also given a distinct 0-indexed integer array removable containing a subset of indices of s (s is also 0-indexed).

You want to choose an integer k (0 <= k <= removable.length) such that, after removing k characters from s using the first k indices in removable, p is still a subsequence of s. More formally, you will mark the character at s[removable[i]] for each 0 <= i < k, then remove all marked characters and check if p is still a subsequence.

Return the maximum k you can choose such that p is still a subsequence of s after the removals.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# EXAMPLE

    Input: s = "abcacb", p = "ab", removable = [3,1,0]
    Output: 2

Explanation: After removing the characters at indices 3 and 1, "abcacb" becomes "accb".
"ab" is a subsequence of "accb".

If we remove the characters at indices 3, 1, and 0, "abcacb" becomes "ccb", and "ab" is no longer a subsequence.

Hence, the maximum k is 2.

# BINARY SEARCH ON ANSWER

The basic idea is that since the range of "k" is from 0 to length of removable list, and this range is in a sorted order, we can apply Binary Search on this range. We are searching for the "Maximum valid value of k".

So for each "mid", we check whether it is valid or not. "mid" is nothing but a possible value of "k". So we will have a helper method to check if after removing the characters at first "k" indices (in "removals") from "s", "p" is still a subsequence of "s". If "mid" is not valid, automatically it makes no sense to check any value of "k" bigger than mid as that won't be valid too.

Otherwise, if "mid" is valid, we will keep searching on right side as we want to "maximize" the "k".