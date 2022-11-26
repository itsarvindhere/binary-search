# PROBLEM STATEMENT

Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

# EXAMPLE

    Input: nums = [1,2,3,4,5], k = 2
    Output: 9

Explanation: There are four ways to split nums into two subarrays.

The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.

# BINARY SEARCH ON ANSWER

We are asked to Minimize the "Largest Sum" after splitting the array into "k" subarrays. So, what can be the lower bound of "Largest Sum" for any list? 

Think what would happen if we have to split the array into subarrays of single elements. 

	For example, if nums = [1,3,4] and k = 3 
	
	which means we have to split array into 3 subarrays

In that case, the "Largest Sum" will simply be the maximum element in the list. That is, "4".

And similarly, what can be the upper bound of the "Largest Sum" for a subarray?

What if we have to split the array into a single subarray? That is, the whole array itself.

	For example, if nums = [1,3,4] and k = 1 

In this case, "Largest Sum" is simply the sum of whole list. That is "8"

And so, it means, for nums = [1,3,4], no matter what the value of "k" is, the largest sum is in the range [4,8]. It cannot be anything less than 4 and anything greater than 8. And so, we have to minimize this value.

Because this range is in a sorted order, that means we can try using Binary Search to minimize the Largest Sum. And that's what we call "**Binary Search on Answer**".

So every "mid" we get in Binary Search is a possible "Minimized Largest Sum" value. So, we have to first check whether there is any way to split the array into "k" subarrays such that the largest sum of any subarray is "mid". And for that, we have a helper method in the code below.

So if we can split the array into "k" subarrays such that the largest sum of any subarray is "mid", it means, "mid" is a valid largest sum value. But since we are asked to "Minimize" this value, we will keep searching on left side of mid.

But, if "mid" value it not valid, that means, no value smaller than "mid" can be valid.  So it makes no sense to search for a valid value on left side of mid. Hence we search on right side in that case.