# PROBLEM STATMENT

You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:

    1. nums.length == n
    2. nums[i] is a positive integer where 0 <= i < n.
    3.abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
    4. The sum of all the elements of nums does not exceed maxSum.
    5. nums[index] is maximized.

Return nums[index] of the constructed array.

Note that abs(x) equals x if x >= 0, and -x otherwise.

# EXAMPLE

    Input: n = 4, index = 2,  maxSum = 6
    Output: 2
    
Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].

# BINARY SEARCH ON ANSWER APPROACH

In this problem, we are asked to "**Maximize**" the value at nums[index]. 

Now think about this. If nums[index] is the maximum possible value in the list, then isn't it the peak value? 

That is, the array keeps increasing till this "index". And then it keeps decreasing. 

And because we are given the condition that two adjacent elements cannot have difference more than 1, it means - 

	If at nums[index] we have a value"x"
	
	Then at nums[index - 1] we can have "x - 1" and same at nums[index + 1]
	Then at nums[index - 2] we can have "x - 2" and same at nums[index + 2]
	
So, how is Binary Search going to help us find the maximum value at nums[index] so that array is valid as per the given conditions?

	Think of what can be the possible values at any index? 
	
	We are given that the value cannot be less than 1 at any index. 
	
	Hence, the lower bound is 1.

	Similarly, what can be the largest possible value? 
	
	Take this scenario where we have an array with n = 1. So there is only 1 element. 
	
	And maxSum is 100. 
	
	Then what is the maximum possible value of that one element? 
	
	Ofcourse it is 100 only. 
	
	Because sum of array should not exceed maxSum. And that's the upper bound.

Hence, at nums[index], the value can be any value between 1 and maxSum (both included). Also, there is monotonicity. That is, if "x" is a valid value that we can put at nums[index], then every value smaller than "x" is also a valid value at that index. 

Similarly, if "x" is not a valid value that we can put at nums[index], then no value greater than "x" can be valid. So in this way, we can check if the "mid" value that we get is valid or not and based on that, we search either on left side of right side of mid.

The most difficult part in this problem is to have some way to check whether the resulting array with nums[index] = mid is a valid array or not. That is, its sum is <= maxSum. And we have to do that without constructing the whole array since if we decide to create the array from scratch, that won't be efficient and will give TLE since "n" can be up to 10^9. In fact, this is also one hint that we have to use Binary Search. Because with this constraint, even an O(N) solution with give TLE for large "n" values. So either we have to write an O(LogN) solution or an O(1) solution.

**THE HELPER METHOD**

In the code, to check if a particular "mid" value can be a valid value at "nums[index]", we have a helper method "isValid". Now, to understand what is going on, we have to take an example.

	Consider this array nums -> [6,7,8,9,10,9,8,7,6]
	
	Suppose, n = 9, index = 4 and maxSum = 70
	
	So, here, we have put value "10" at index 4 
	and we can see it is a valid array as its sum is 70 which is <= maxSum.
	
	Now, how to calculate its sum without constructing this array? All we know are four things - 
	
		1. n -> length of array
		2. index -> index at which we have set some value "x"
		3. x -> the value that we have set at "index"
		4. maxSum -> The total sum of array should not exceed this maxSum value

We already discussed above that whatever value we have at "index", it should be the "peak" value only then it will be maximized. And here too, we have the same scenario. 10 is a peak value. 

Now, is there some way to calculate the sum of subarray on the left and right side of the "index" in O(1) time? Indeed there is. Because if you notice, on the right side of "10", we have [9,8,7,6]. 

	We know that to calculate sum of first "n" natural numbers, we do - n * (n + 1) / 2 
	
	So, to calculate the sum from 6 to 9, what we can do is -
	
		1. Calculate sum from 1 to 5
		2. Calcaulte sum from 1 to 9
		3. Substract 1 from 2 to get the sum from 6 to 9

	But will this be the case with every test case? NO!
	
Why? Because for some test cases, there will be more slots to fill on right and left side such that we will have extra 1s.

Take another example for that. 

	nums = [2,3,2,1,1,1]
	index = 1, x = 3, maxSum = 10
	
	Here we see that, subarray on right of "3" is [2,1,1,1]
	
	So, while we can calculate the sum of [2,1] using the same formula as above, what about [1,1]
	
	WE don't know beforehand how many extra 1s we have to add. 
	
	So to calculate that, first we need to find how many spaces we have to fill on right and left side of "index".
	
    If you see in  [2,3,2,1,1,1], there are "4" spaces to fill on right side of index "1"
	
	And n = 6.
	
	So ofcourse there are "n - x - 1" spaces on right side of "index".
	
	Similarly, for left side, the number of spaces to fill is simply "index". 
	
	For example here, index = 1 which means, there is 1 space to fill on left of "index"
	
So now, from these empty spaces, we can figure out whether we have to add extra 1s or not. If not, then simply we can do what we did in case of [6,7,8,9,10,9,8,7,6]. 

Now think about this. If at "index", we have put a value "x". And it is a peak value which means after and before it, we have values in this fashion -
	
		[...x - 3, x-2, x-1, x, x-1, x-2, x-3...]
		
Then ofcourse we cannot just keep doing 'x - whatever' since a value cannot be less than 1. This means, if the empty spaces on the right or left side of "index" are more than or equal to "x", then in that case, we will have to add some extra 1s. Otherwise not. 

	For example - 
	nums = [2,3,2,1,1,1]
	index = 1, x = 3, maxSum = 10
	
	Here, rightSpaces = n - index - 1 => 4
	leftSpaces = index => 1
	
	And we see that there are 4 spaces to fill whereas x is 3. And since 4 >= 3, it means, we will have to add some extra "1" on right side.
	
	How many? Well, that is simply -> (4 - 3) + 1 or "(rightSpaces - x) + 1"
	
	 So, in this case we see, right subarray is [2,1,1,1]
	 
	 So first, we can calculate the sum of [2,1] using the formula n * (n + 1) / 2
	 
	 And then, we can add the extra 1s we added. That is -> 2.
	 
And now, our Helper method is ready. All we want to do now is to find if the totalSum that we got is <= maxSum or not. Only then the particular "x" value will be valid.

	TotalSum => LeftSum + RightSum + x
	
We have to add "x" separately because if you notice, leftsum is sum of elements to left of x and rightsum if sum of elements to right of x. We did not include "x" in any of these two sums. Hence, finally, we have to add it separately to get the totalSum of the resulting array.