# PROBLEM STATEMENT

You are given two non-increasing 0-indexed integer arrays nums1​​​​​​ and nums2​​​​​​.

A pair of indices (i, j), where 0 <= i < nums1.length and 0 <= j < nums2.length, is valid if both i <= j and nums1[i] <= nums2[j]. The distance of the pair is j - i​​​​.

Return the maximum distance of any valid pair (i, j). If there are no valid pairs, return 0.

An array arr is non-increasing if arr[i-1] >= arr[i] for every 1 <= i < arr.length.

# EXAMPLE

    Input: nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
    Output: 2

Explanation: The valid pairs are (0,0), (2,2), (2,3), (2,4), (3,3), (3,4), and (4,4).
The maximum distance is 2 with pair (2,4).

# BRUTE FORCE APPROACH - O(N^2)

The Brute Force approach is pretty simple. For each element, go through each element in second list that is greater or equal and keep calculating the maxDistance. Not efficient and will give TLE for large arrays. But from this, we can start thinking about optimizing our solution.


# BINARY SEARCH APPROACH - O(NLogN)

Because it is given that both the arrays are sorted in decreasing order, it means, instead of linear search on second array, we can perform Binary search.

    What do we have to search?

    We have to search for the maximum possible value of "j" such that 
    the element at "j" index is >= particular element in the first list

If the element at mid satisfies the condition, it might be a possible solution but it is also possible that we may find an element after it that also satisfies the condition. In that case, we will get a larger distance. Hence, even if mid satisfies the condition, we continue searching on right side of mid.

# TWO POINTERS APPROACH - O(N)

Using Two Pointers approach, we can do this problem in an O(N) time complexity which means this is the fastest solution among the three. 

We start with both the pointers at the beginning of both lists as i <= j

And now, we will compare the elements and check whether num2[j] >= num1[i]. If yes, calculate the distance and update the maxDistance if this distance is bigger than previous. And also, since we are looking for the maximum possible distance, we will also increment j. 

But if num2[j] < num1[i], that means not only this element does not satisfy the condition, but no element after it will satisfy because array is sorted in decreasing order. Hence, it means we are done with nums1[i] and so, we can move on to the next ith index element.

	Example - nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
	
	Initially, i = 0, j = 0, maxDistance = 0
	
	So, we see that num1[i] = 55 and num2[j] = 100
	
	Since 100 >= 50. We calculate the distance and it comes out to be 0 since j - i => 0 - 0 => 0
	
	Since we want to maximize the distance, we increment j. 
	
	Now, i = 0, j = 1, num1[i] = 55 and num2[j] = 20
	
	Is 20 >= 55? NO! It means, no element after it is valid as well. So, for 55, we are done. Increment i.
	
	Now, i = 1, j = 1, num1[i] = 30 and num2[j] = 20
	
	Is 20 >= 30? NO. Again, increment i.
	
	We see that here, i = 2 and j = 1. This violates the condition that says i <= j. 
	
	Hence, to make sure this condition is not violated, if i becomes > j when we increment it, we will also increment j.
	
	And this process continues till =>  i <len(nums1) and j < len(nums2