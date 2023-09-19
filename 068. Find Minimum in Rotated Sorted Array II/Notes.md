# PROBLEM STATEMENT

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.

# EXAMPLE

Input: nums = [2,2,2,0,1]
Output: 0


# APPROACH

First, let's understand how can we find minimum in a rotated sorted array. Since array was sorted before it is rotated, it means we can make use of Binary Search here.

    Consider an example -> [2,2,2,0,1]

When we use Binary Search, then we will get start element as "2", end element as "1" and mid element as "2"

Now, if you look closely, since the array is rotated, it is divided into two parts. One is [2,2,2] and the other is [0,1] because initially the array as [0,1,2,2,2]

And the elements in left part will always be bigger than all the elements in the right part. 

This means, what we want to check is whether "mid" element belongs to left subarray or right subarray. if it belongs to the "left" subarray,then we know we will not find minimum on left side of mid. But if it belongs to the right subarray, then it means, we will find the minimum on the left side of mid.

    "mid" will belong to left subarray if nums[mid] >= nums[start]

Here, we see "start" and "mid" are the same i.e., "2". And since nums[mid] >= nums[start], So, we will move towards the right side for the smaller element. Before that, we will also check if "mid" is smaller than the previous smaller element (initially, we assume the first element is the smallest, just like how it is in case of a sorted array that is not rotated).

Now, start element = 0 and end element = 1. We see that here, start element itself is smaller than end element which means there is no need to even go to the right side. Since start is smaller than end, that means, either the previous mid element was the minimum, or the "start" element is the minimum. We simply return whatever is smaller.

So here, we will return 0 as the minimum element.

Hence, for every mid, we will also check if it is smaller than previous mid or not and update our minimum element accordingly. And after that, we move to either left or right side of mid.


## 1. APPROACH #1 - FIRST REMOVE THE DUPLICATES

Since this problem asks us to decrease the operations as much as possible, this is not the best solution. But basically, we wil remove the duplicates and it then becomes "[Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)" problem.

## 2. APPROACH #2 - SIMPLY USE BINARY SEARCH WITH A LITTLE TWEAK

If you use the same code as above (without removing duplicates), then you will see 187/193 test cases are getting passed. 

One test case that is failing is [10,1,10,10,10]. So, let's see how to fix that.

    [10,1,10,10,10]

    start = 10
    end = 10
    mid = 10

    Did you see the problem? All the pointers have same element.

    So, as per above code's logic, 
    since mid >= start, we should move to right side. 

    But this means, we will lose the actual minimum element 
    which is "1".

In this case, the minimum can be anywhere. It can be on right of mid or on the left of mid.Here, it is on the left side of mid but if we had [3,3,0,3] then it would've been on the right side of mid.

So, to avoid any issues with any test case, we will increment start and decrement mid and we will do this till we are sure that mid, start and end are not all the same.

And  that's the only extra step required in this problem. The rest of the code is exactly same as for "Find Minimum in Rotated Sorted Array" problem.