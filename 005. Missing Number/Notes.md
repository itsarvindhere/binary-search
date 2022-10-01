# PROBLEM STATEMENT

Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.


# EXAMPLE

    Input: nums = [3,0,1]
    Output: 2
    Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

# BINARY SEARCH APPROACH - O(nlogn) Time and O(1) Space

We want to "search" for a missing number so why not make use of Binary Search here?

But before using Binary Search, the array has to be sorted so that's why, the complexity here is O(nlogn)
If the array was already sorted, it would've been O(logn) and this would've been a more efficient approach than xor solution.

So, what would be the strategy using Binary Search in this problem?

Read the problem statement carefully. It says the numbers are in the range [0,n]

What this means is that if array is sorted, then at each index, the number present is same as that index.

e.g. [0,1,2]

If this is the array we have, then at 0th index, we have 0. At 1st index we have 1. At 2nd index we have 2. So that's the pattern here.

For this example, answer will be 3 since the length is 3 and 3 is not present in this array but that is an edge case. 

For now, lets talk about missing elements in range 0 to n-1 because we can search them using Binary Search.

	Example -> nums = [9,6,4,2,3,5,7,0,1]
	
	First, we sort this array.
	After sorting, nums = [0,1,2,3,4,5,6,7,9]
	
	And now, we apply binary search. But what are we searching for? 
	We are searching for an index at which element is not equal to index, 
	which should be the case with a valid array. 
	
	
	Initially start = 0 and end = n - 1 or 8
	
	Mid is 4. At index = 4, we have 4. 
	This shows that till 4th index, all elements are available and are at their correct place
	
	So it makes no sense to search for missing element on left of mid. Hence, we will search on the right  side of mid.
	
	start becomes mid + 1 => 5
	end is still 8
	
	New Mid = 6
	
	Again we see at index = 6, we have 6. 
	So till 6th index as well, all elements are present and are at correct place.
	
	start becomes mid + 1 => 7
	end is still 8
	
	New Mid = 7
	
	Same story as above.
	
	start becomes mid + 1 => 8
	end is still 8
	
	And now, we get mid = 8
	
	We see that at index 8, we have 9. 
	But since 8 should have been there at this index, 8 is missing number. 
	
	Hence we will return 8 in this case.
	

## **DO WE RETURN AS SOON AS WE FIND THE MISSING NUMBER AT MID?**

The answer is - "NO". 

Take this example -> 
			
					nums = [2,1,3]
					
					After sorting, nums = [1,2,3]
					
					If we apply binary search, mid will be index = 1 and element at index = 1 is 2
					
					So does that means 1 is missing? 1 is present in array. 
					
If at mid index element is not correct, that means either one of the two cases are true - 
	1. mid index is the missing element
	2. There is a missing element on left of mid which is causing the current mid index to have incorrect element
							
And that's the whole point. Even if we see that mid index does not have correct element, we should not stop. We should store that index somewhere (as it can be the missing element) and then continue searching on left of mid.


# XOR APPROACH - O(n) Time and O(1) Space**

When we XOR two numbers then if two numbers are the same then the XOR is 0. This is something we all know, right?

Here, the important thing to note is that array has distinct elements in range [0,n] (n included as well)

So it means the index will also be in the range [0,n]. This means, for any array with a missing number, if we XOR the indexes and the elements, then eventually we will get back the missing element.

e.g. arr = [0,1,3]
Here since n is 3 that means this array should have all numbers from 0 to 3 but it is missing 2. Lets use XOR to find that.

Since indexes will also be in range 0 to 3, we will first XOR the indexes andthen XOR the numbers.

	XOR1 = 0 ^ 1 ^ 2 ^ 3  //XOR of the indexes that range from 0 to 3
	XOR2 = 0 ^ 1 ^     3  //XOR of the elements of given array
	
And now, if we do XOR1 ^ XOR2, all the similar elements will cancel out each other so eventually, the result will be 2 which is the missing number!