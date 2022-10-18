# PROBLEM STATEMENT

You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].

Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

# EXAMPLE

    Input: arr = [1,2,3,5], k = 3
    Output: [2,5]

Explanation: The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
The third fraction is 2/5.

# HEAP SOLUTION - O(N^2)

The simplest solution we can think of is a Heap Solution in which we keep track of k smallest fractions by maintaing a max heap of k size. WE use a max Heap because we want to discard all the bigger fractions from top and only keep the smaller ones. In the end, the top of heap will have the kth smallest fraction.

# BINARY SEARCH ON ANSWER APPROACH

We are asked for the kth smallest fraction. What can be the range in which the kth smallest fraction will be?

In other words, what is the range in which any possible fraction in the given input array will be? 

It will be the range 0 to 1. Why?

because it is given that we have to consider only those fractions where i < j and since this is a sorted array , it means the numerator will always be smaller than denominator, meaning the fraction will never be more than 1 for any two pairs. In fact, it cannot even be exactly 0 or 1 but we can take 0 as lower and 1 as upper bound for our Binary search.

So, when we find a mid value, we need to see how many fractions are there that are less than (or equal to) that mid value. And if there are exactly k values, then that means, we can take the largest fraction out of those and that will be the kth smallest fraction.
