# PROBLEM STATEMENT

The frequency of a value in a subarray is the number of occurrences of that value in the subarray.

Implement the RangeFreqQuery class:

    1. RangeFreqQuery(int[] arr) Constructs an instance of the class with the given 0-indexed integer array arr.
    2. int query(int left, int right, int value) Returns the frequency of value in the subarray arr[left...right].


A subarray is a contiguous sequence of elements within an array. arr[left...right] denotes the subarray that contains the elements of nums between indices left and right (inclusive).


# EXAMPLE

    Input
    ["RangeFreqQuery", "query", "query"]
    [[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]
    Output
    [null, 1, 2]

Explanation:

RangeFreqQuery rangeFreqQuery = new RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]);
rangeFreqQuery.query(1, 2, 4); // return 1. The value 4 occurs 1 time in the subarray [33, 4]
rangeFreqQuery.query(0, 11, 33); // return 2. The value 33 occurs 2 times in the whole array.


# DICTIONARY + BINARY SEARCH APPROACH

All we have to count is in a particular subarray, how many times a value occurs. 

So, we can have a HashMap that we will use to keep track of at what index a value appears in the given array. So for example, if the array that we are given is - 

		[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]
		
		Then we will create a HashMap like - 
		
			{
				12: [0, 9], 
				33: [1, 7], 
				4: [2], 
				56: [3, 11], 
				22: [4, 8], 
				2: [5], 
				34: [6, 10]
			}
			

Hence, for each element, we have a list of indices at which it appears in the given array. And ofcourse each list will be in a sorted order.

Now, when we call the "query" method with some "left", "right" and "value" arguments, then all that we have to do is for that "value", take its list from the dictionary, and apply Binary Search.

	How are we going to use Binary Search here?
	
	Suppose, 
				left = 0
				right = 11
				value = 33
	
	It means, in the subarray starting at index 0 and ending at index 11 (both included), how many times "33" appears.
	
	We know that for "33", the list in the dictionary is ->  [1, 7]
	
	And if you see, the smallest index in this list is "1" and it is greater than the left value i.e., 0.
	Similarly, the largest index is "7" and it is smaller than the right value i.e, 11
	
	Hence, both these indices lie in this subarray. In other words, 33 occurs twice in this subarray.
	

And that's the whole idea of Binary Search here. We will first search for the smallest index in the list that is >= left
And then, we will search for the largest index in the list that is <= right

	Once we find these two indices, count = (rightIndex - leftIndex + 1)
	
Also, if the leftmostIndex comes as -1, that simply means not even a single occurance of "value" is there in the subarray. So we can straight away return 0 in that case instead of extra unnecessary computations.