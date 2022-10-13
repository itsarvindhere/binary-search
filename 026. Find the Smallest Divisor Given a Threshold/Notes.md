# PROBLEM STATEMENT
Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.

Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).

The test cases are generated so that there will be an answer.

# EXAMPLE

    Input: nums = [1,2,5,9], threshold = 6
    Output: 5

Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 

# BINARY SEARCH ON ANSWER - APPROACH

Yet another problem that can be solved using "**BINARY SEARCH ON ANSWER**" concept.

Here, we are asked for the smallest divisor that mets the condition.

	So, what is the range of valid solutions/divisors ?

	The smallest possible divisor can be 1. 

	And regarding the largest possible value, it can be the largest value in the list. 

	So we get a range as 1 to Max(nums)

And this range is in sorted order which means we can use Binary Search on this range to search for the Smallest valid Divisor. 


So, all we need to do now is the check if "mid" is valid or not. If "mid" is valid divisor, all values bigger than it are also valid. But if it is not valid, that means, any value that is less than it are also not valid.

If "mid" is valid, all values after it are also valid. But since we are asked for "Smallest" divisor, we need to look for a smaller number than "mid" that is valid. So that's why we move to left of mid in that case.

But if "mid" itself is not valid, then no value before it can be valid. Hence, in that case, simply search on the right of mid.