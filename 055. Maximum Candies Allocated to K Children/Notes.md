# PROBLEM STATEMENT

You are given a 0-indexed integer array candies. Each element in the array denotes a pile of candies of size candies[i]. You can divide each pile into any number of sub piles, but you cannot merge two piles together.

You are also given an integer k. You should allocate piles of candies to k children such that each child gets the same number of candies. Each child can take at most one pile of candies and some piles of candies may go unused.

Return the maximum number of candies each child can get.

# EXAMPLE

    Input: candies = [5,8,6], k = 3
    Output: 5

Explanation: We can divide candies[1] into 2 piles of size 5 and 3, and candies[2] into 2 piles of size 5 and 1. We now have five piles of candies of sizes 5, 5, 3, 5, and 1. We can allocate the 3 piles of size 5 to 3 children. It can be proven that each child cannot receive more than 5 candies.

# BINARY SEARCH ON ANSWER

This is one of those problems where we can use **Binary Search on Answer** concept.

In this concept, we first figure out the range of all the possible values of whatever we are asked to find. For example, we are asked to find the "Maximum Candies Each Child can get". So, we can think of what can be the smallest possible valid value and what can be the largest possible valid value, for any test case. 

It is pretty obvious from the given example that it is also possible that we cannot distribute a single candy to each child. It means, the smallest possible valid value for "Maximum Candies each child can get" is 0.

And now, for the largest possible valid value, the hint that the problem gave is "**Each child can take at most one pile of candies**". Since a child can take at most one full pile, it means, the maximum possible valid value can be the maximum candies in any pile.

	And now, we get this range -> [0, max(candies)]

Since this range is sorted, we can apply Binary search on this one. All we want is to maximize the valid value. That is, if "mid" is valid, store it and keep searching for a higher valid value on its right side. It makes no sense to search on left side of "mid" if "mid" is valid. Take the above example. If we can distribute "5" candies to each child, then of course we can also distribute "4" or "3" or "2" or "1" candy to each child.

Similarly, if "mid" is not valid, there is no need to search on right side as all values higher than "mid" will be invalid too. That is, if we cannot distribute "6" candies to each child, we cannot distribute "7" or "8" or any candy count higher than "6" as well.