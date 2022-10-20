# PROBLEM STATEMENT

Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.


# EXAMPLE

    Input: nums = [2,2,3,4]
    Output: 3

    Explanation: Valid combinations are: 
    2,3,4 (using the first 2)
    2,3,4 (using the second 2)
    2,2,3

# BRUTE FORCE - O(N^3)

The most straightforward way is to have three nested loops and try to find all the combinations of sides a,b and c such that -

		a + b > c
		a + c > b
		b + c > a

# BINARY SEARCH - O(N^2 * LogN)

If we sort the given list, then we can use Binary search to get the time complexity down from O(N^3) to O(N^2 * LogN). As you can notice, we will do that by using Binary Search on the inner most loop instead of linear search i.e., O(N) to O(LogN)

	Lets take  nums = [2,2,3,4]
	
	So, we will still have two nested for loops for two sides. So initially,
	
	we have 
	
		a = 2
		b = 2
		
	And we want to search a side c. 

What should be the criteria to search side c? How can we say if a particular side "c" is valid?
	
	Notice the conditions - 
	
			a + b > c
			a + c > b
			b + c > a
	
	Since we have sorted our list, that means "c" will always be bigger or equal to a and b. 
	
	That also means, 
			
				a + c > b 
				  and 
				b + c > a
				
	will always be true for any value of "c" because c is >= a and c >= b
	
	
	So the only condition left is a + b > c
	
	Since the array is sorted, that means if we can find the largest possible value of "c" 
	such that it is still smaller than "a +b", 
	then all the numbers in between will be all the value values of third side.
	
	e.g. [2,2,3,4]
	
	Since a = 2 and b = 2
	
	We start binary search from value 3 (index = 2)
	
	We get mid = index 2 at which we have 3. 
	
	Now we check if a + b > c or not.
	
	Since 2 + 2 > 3, that means, 3 is a valid value for a third side if first and second side is 2 and 2 respectively.
	
	But we won't stop here. Can we find a value bigger than 3 that also satisfies this condition? 
	
	So we continue. Next, mid = index 3 at which we have value = 4
	
	Now we check if a + b > c. 
	
	Since 2 + 2 > 4 is not correct, that means, 4 cannot be a valid third side length if a = 2 and b = 2
	
	Hence, for a = 2 and b = 2, we can have only one valid value as third side.


This means, once we find the largest value for third side such that a + b > c, we can use any value that is between the index of b and the largest value we found via binary search (both included) to make a triangle. Hence, we increment our count by the number of values between "b" index and the index of the largest valid value we got via Binary Search.

# OPTIMIZED BINARY SEARCH

Once we find an index after performing Binary Search, then for the next value of "j", instead of again performing binary search starting from "j + 1" index, we can start from the index we got from previous binary search.
​
So, for a particular pair (i, j) chosen, when we choose a higher value of j for the same value of i, we need not start searching for the "res" from the index j+2. Instead, we can start off from the index "res", directly where we left off for the last j chosen.

This holds correct because when we choose a higher value of j(higher or equal nums[j] than the previous one), all the nums[k], such that k < k(i,j) will obviously satisfy nums[i] + nums[j] > nums[k] for the new value of j chosen.

