# PROBLEM STATEMENT

(This problem is an interactive problem.)

You may recall that an array arr is a mountain array if and only if:

    1. arr.length >= 3
    2. There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

# BINARY SEARCH APPROACH

This is a really easy problem if you just observe the examples a little.

We want the "minimum" index of an element in an array. It just means, the "first occurance" or the element in the given array. That's it. That's the point of this problem.

We know that in case of a regular array that is in increasing order or decreasing order, to find the first occurance, all we do is, try to check if that element is present at "mid" or not. If yes, we will save that index, and keep searching on left to find the first occurance. 

Here, we are given a Mountain Index. A Mountain Index has a "Peak" index which means, [start, peak] is in increasing order whereas the [peak, end] is in decreasing order.

Now, you can understand that all that we need here is to first find this Peak index. Once we get hold of that, we can easily Binary search on [start, peak] and [peak, end]. 


	Take an example -> array = [1,2,3,4,5,3,1], target = 3
	
	Here, first we will find the peak element and we get it has "5". Its index is 4.
	
	So now, we know that from index 0 to index 4, we have an array sorted in increasing order
	And from index 4 to index 6, we have an array sorted in decreasing order
	
