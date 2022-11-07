# PROBLEM STATEMENT

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

# EXAMPLE

    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]


# BINARY SEARCH APPROACH

We need to find the first and last position of an element in an array. And since it is given that the array is sorted, we can use Binary Search to do it in O(LogN) time complexity. 

To find the first occurance of any element in a sorted array, what we do is, even after we found the element at mid position, we still continue our search on left side of mid so that we are sure that at the end, the index we get is the "first occurance".

Similarly, to find the last occurance of any element in a sorted array, even after we found the element at mid position, we still continue our search on right side of mid so that we are sure that at the end, the index we get is the "last occurance".

And if the first occurance itself is -1, there is no point of again running Binary Search for last occurance. So in that case, we can straight away return [-1,-1]