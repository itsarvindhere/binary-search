# PROBLEM STATEMENT

You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

# EXAMPLE

    Input: nums = [3,5]
    Output: 2
    Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

# 1. BRUTE FORCE APPROACH - O(N^2)

n Brute Force Approach, we have two nested loops and for each valid value of x, we have to go through the whole list and count how many numbers are >= x. If the count is == x, that means this is a special array and we can return x.

But again, we have to loop through the whole array for each x. So not an efficient approach.

# 2. BINARY SEARCH APPROACH - O(NLogN)

We can sort the array in increasing order and now, all we need to find is the index of the smallest number that is >= x. 

If we find that index, we know that all elements after that index are also >= x since array is sorted. So we are not traversing the whole list for each value of x. 

In Binary Search, we will either move to right of mid or left of mid so this is a much better approach than the Brute Force approach.

# 3. COUNTING SORT - O(N)

The most efficient solution for this problem is using counting sort.

Basically, we will store the count of each element in the given array in a new array.

And use that count to calculate how many elements are >= any x value. 

			nums = [0,4,3,0,4]
			count = [2,0,0,1,2]

Each index value specifies what is the count of number = index in the given array. e.g. count of 0 is 2, count of 1 is 0 and so on...

Now that we got this array, how to find how many elements are >= any x value? 

As we know, the range of x is from 0 to length of the given array (inclusive). Because obviously it cannot be more than length as we know there can be an x that is <= to all the numbers of given array so for that case, length of array will be the result.

So, for each value of x from 0 to n, we need to check what is the count of x in the count array. Just think about it. Each value in count array shows how many times a particular number appears in the array. So that means, each value in count array means how many elements are == x.

    Take 0 for example in nums = [0,4,3,0,4]

    count = [2,0,0,1,2]
	
	Count of 0 = 2
	So, there are 2 elements that are equal to 0
	
	And Because 0 is the smallest possible value in the array. So obviously all elements of array are >= 0
	
	But then when x becomes 1. Then we see count of 1 = 0.
	
	But wait. We know that if x == 1, we only need to count numbers >= 1. So we don't need the count of 0s now.
	
	In other words -> Count of numbers >= 1  ->
	
			(Length of array - count of 0 in array)
	  
	 And for this reason, after each iteration, we have ti remove the count of current x from n.