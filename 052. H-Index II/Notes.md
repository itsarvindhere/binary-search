# PROBLEM STATEMENT

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper and citations is sorted in an ascending order, return compute the researcher's h-index.

According to the definition of h-index on Wikipedia: A scientist has an index h if h of their n papers have at least h citations each, and the other n − h papers have no more than h citations each.

If there are several possible values for h, the maximum one is taken as the h-index.

You must write an algorithm that runs in logarithmic time.

# EXAMPLE

    Input: citations = [0,1,3,5,6]
    Output: 3

Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had received 0, 1, 3, 5, 6 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.


# **1. BRUTE FORCE - O(N^2)**
Since the h-index can be at least 0 and at most N, it means we can go through each possible h-index and for every h-index value, try to see if this can be a valid h-index. But since the length of input list can be up to 10^5, this is not an efficient solution and will give TLE. 

It works for the other H-Index Problem, though -> https://leetcode.com/problems/h-index/
		
# **2. BINARY SEARCH ON ANSWER #1 - O(NLogN)**

Since we know that the range of possible h-index values is sorted already (0 to N), why are we doing a linear scan? Why not use Binary search on this range? All we want to do is maximize the h-index.

It works for the other H-Index Problem, though -> https://leetcode.com/problems/h-index/

# **3. BINARY SEARCH ON ANSWER #2 - O(LogN * LogN)**

Along with the range, the given input list is already in a sorted order. This means, instead of a linear search to find how many papers have at least "mid" citations, we can use Binary Search for that too.

# **4. SIMPLE BINARY SEARCH - O(LogN)**

This is what the Problem asks us to write - A solution with Logarithmic time complexity. (Check out the code comments for better explanation)