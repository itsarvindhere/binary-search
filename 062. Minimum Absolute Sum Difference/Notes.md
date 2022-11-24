# PROBLEM STATEMENT

You are given two positive integer arrays nums1 and nums2, both of length n.

The absolute sum difference of arrays nums1 and nums2 is defined as the sum of |nums1[i] - nums2[i]| for each 0 <= i < n (0-indexed).

You can replace at most one element of nums1 with any other element in nums1 to minimize the absolute sum difference.

Return the minimum absolute sum difference after replacing at most one element in the array nums1. Since the answer may be large, return it modulo 109 + 7.

# EXAMPLE

    Input: nums1 = [1,7,5], nums2 = [2,3,5]
    Output: 3

Explanation: There are two possible optimal solutions:
- Replace the second element with the first: [1,7,5] => [1,1,5], or
- Replace the second element with the third: [1,7,5] => [1,5,5].
Both will yield an absolute sum difference of |1-2| + (|1-3| or |5-3|) + |5-5| = 3.

# BINARY SEARCH APPROACH

For once, suppose we are simply asked to return the absolute sum difference. 

	Suppose, nums1 = [1,7,5], nums2 = [2,3,5]
        
	 So, abs sum difference is |1-2| + |7-3| + |5-5| = 5
        
Now add in what we are asked to do. 

	We are asked to take an element in nums1 and replace it with any other element in nums1
	
	So that, we can get an absolute difference smaller than 5
        
	Suppose we replace "1" by "5"
	In that case, the new abs sum diff will become -> |5-2| + |7-3| + |5-5| = 7
	But this did not reduce the difference. Instead it increased it from previous value.
        
	So, will replacing "1" by "7" give us a smaller value? NOPE!
	
	Because if replacing it by "5"did not give us a smaller value, "7" won't give us a smaller value as well.
	
	So basically, we got the idea that we want to replace such that 
	
	the new absolute difference is smaller than the one we got without any replacement.
	
	
Now the question is, for an element, how can we find by which element we should replace it so that the absolute difference with nums2[i] can be minimized? Well, it is quite simple. Just find the "floor" and "ceil" values.

		nums1 = [1,7,5], nums2 = [2,3,5]
		
		For "7", its corresponding value in nums2 is "3"
		
		Initially, abs diff is | 7 - 3 | => 4
		
		Now, by what value can we replace "7" to make sure we get the smallest possible abs difference from 3
		
		Well, that value is either floor of "3" or ceil of "3" in nums1.
		
		Floor means largest value that is <= "3"
		Ceil means smallest value that is >= "3"
		
		Here, floor of "3" is "1"
		And ceil of "3" is "5"
		
		Now think about it. Originally, the difference was "4".
		
		If we replace "7" by "1", difference will be | 1 - 3 | => 2
		If we replace  "7" by "5" difference will be | 5 - 3| => 2
		
		And so, both these are not only same but also smaller than the original difference of "4"
		
		Replacing "7" by "1" or "5" will reduce the original difference from "4" to "2". That is, it will reduce it by a value "2".
		
		And this value is what we are keeping in the "maxAbsDiffVal" variable in the code. 
		
		That is, by how much we are reducing the initial absolute difference.

		If we consider "1", then for it, initial abs difference will be | 1 - 2 | => 1
		
		We can replace it by "5" as that is the ceil value and it will give us a new abs difference of | 5 - 2| => 3
		
		But because this new value is not smaller than initial, that means, replacing "1" by "5" will not work.
		
		Hence in this case, diff - abs(ceil - nums2[i])) will give us a negative value 
		
		which means, "maxAbsDiffVal" remains unchanged in the code for this case.
		
		Similar case if for "5" because already |5 - 5| = 0 is the minimum possible abs diff we can get
		
		so replacing it with any other number will only increase the difference.
		
Hence, to conclude, we want the maximum possible value "maxAbsDiffVal" and this value suggests why how much we have reduced a certain abs difference between two values, by replacing one value with some other value from the same list. This maximum value will reduce the overall sum by the biggest margin and hence in that case we will get the Minimum Absolute Sum Difference, exactly what the problem asks.