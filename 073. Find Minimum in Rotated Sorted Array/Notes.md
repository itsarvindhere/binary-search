# PROBLEM STATEMENT

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

 - [4,5,6,7,0,1,2] if it was rotated 4 times.
 - [0,1,2,4,5,6,7] if it was rotated 7 times.

Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

# EXAMPLE

    Input: nums = [3,4,5,1,2]
    Output: 1

Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# APPROACH

The problem asks us to write a solution in O(LogN) time, which basically means solve the problem using Binary Search.

Before we apply binary search, we have to analyze the examples and see how rotating a sorted array changes the order of elements.

	Suppose, we have nums = [4,5,6,7,0,1,2]
	
	We can see that the list is now divided into two separate sorted lists.
	
	That is, [4,5,6,7] and [0,1,2]
	
	And since these are both sorted, it won't be difficult to find 
	what is the smallest element in these two parts, right?
	
	In Binary search, we take start and end as 0th and last indices initially.
	
	Here, start = 0, end = 6
	
	So, mid will be index 3
	
	Now, at mid index, we have element "7"
	
	We first want to know in which sorted part this element belongs.

	Does it belong to left sorted part of right sorted part?
	
	Here, we see that "7" belongs to the left sorted part [4,5,6,7]
	
	And so, we can say that in this part, the smallest element is "4".
	
	This could be our answer so for now, we will store it in some variable, let's call it "minimum"
	
	minimum = 4
	
	Now, we are done with this left part. So, we can now completely eliminate this left sorted part.
	
	start = mid + 1 = 4
	end = 6
	
	
	Now, the new mid will be 5
	
	At index 5 we have the number "1"
	
	Again, we check to which sorted part it belongs.
	
	We can see that both the parts are sorted to which it belongs. That is [0,1] and [1,2]
	
	So, let's say we will always check for left sorted part first. And since it belongs to left sorted part,
	We will again do the same as above. We will take the smallest in this left sorted part, which is 0
	
	And update the minimum if this new minimum is smaller than previous.
	
	minimum = 0
	
	start = mid + 1 = 6
	end = 6
	
	mid = 6
	
	And at mid, we have "2". minimum is not updated as 0 < 2.
	
	And binary search ends.
	
	And you can check for right sorted part first. It will not affect the solution in any way.
	
So, finally, the minimum element in the rotated sorted array is "0".    
      


 