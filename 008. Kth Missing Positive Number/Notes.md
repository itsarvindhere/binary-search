# PROBLEM STATEMENT

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

# EXAMPLE

    Input: arr = [2,3,4,7,11], k = 5
    Output: 9
    Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.


# 1. COUNTING SORT APPROACH - O(N)

The counting sort approach is pretty straightforward. Just store count of all elements from range 1 to 1000 and then use a counter variable to keep track of how many elements have count = 0 in given array.

We stop as soon as out counter variable becomes 0, we know we found the kth missing element.

There might be test cases when the missing number lies outside the range of given array so in that case, missing number is basically length of array + k

# 2. BINARY SEARCH APPROACH - O(LogN)

To use Binary Search, we first need to understand what to search? 

Lets say we are at mid position. What is the criteria based on which we either move to left of mid or right of mid?

We are given that the range of numbers is from 1 to 1000. So ideally, for a sorted array with no missing numbers, each index should have element = index + 1, right?


Since we want the "Kth" missing number, it means, there can be multiple missing numbers in the array. So, at the mid position, the criteria is to check how many numbers are missing till this mid position. Now the question is how to check that.

	e.g. arr = [2,3,4,7,11], k = 5
	
	If we apply binary search, initialy, mid will be index = 2 at which we have 4
	
	Just by looking at this array, how many elements are missing till index = 2? 
	
	We can see 1 is missing. So there is 1 missing element.
	
	This means, if 1 was there, then at index = 2, we would have 3, instead of 4. 
	
	Hence at mid, we do not have the element that should be there.
	
	So, missing numbers till mid => (Current element at mid - Element that should be at mid)
	
	Hence here, count of missing numbers till index = 2 => 4 - 3 => 1
	
	So we have 1 missing number till mid. But we are asked for 5th missing. So we can never find it on left of mid. 
	
	Hence, we will search on right of mid.
	

This is the idea of this Binary Search approach.

When Binary Search ends, you will see that the "end" pointer will point to the index of the largest element < kth missing.

	e.g. if we continue binary search in above example
	
	arr = [2,3,4,7,11], k = 5
	
	When we move to right of mid, start = mid + 1 => 3 and end = 5
	So new mid = index 4.
	
	At index = 4, we have 11. So again we check how many missing numbers are there till mid. 
	
	Count of Missing Numbers = 11 - 5 => 6
	
	beause ideally, there shoud be 5 at index 4, not 11. So there are 6 missing numbers.
	
	And now we see that k <= 6. Which means, we can find the kth missing on the left side of mid now. 
	
	So, start = 3, end = mid - 1 => 3
	
	mid = 3
	
	AT mid, we have 7. So we again check the same.
	
	Count of missing = 7 - 4 => 3
	
	And since 3 < k, we should move to right of mid. 
	
	So start = mid + 1 => 4, end 3
	
	But now our Binary Search condition becomes false since condition says "start <= end"
	
	So we come out of loop.
	
	Finally, end pointer points to index = 3 at which we have element = 7.
	
	And indeed, 7 is the largest element in this array that is smaller than 5th missing number (which is 9)
	
So, the kth missing number is -> (end index + k + 1) => (3 + 5 + 1) => 9