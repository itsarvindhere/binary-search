# PROBLEM STATEMENT

You are given a 0-indexed array nums comprising of n non-negative integers.

In one operation, you must:

    Choose an integer i such that 1 <= i < n and nums[i] > 0.
    Decrease nums[i] by 1.
    Increase nums[i - 1] by 1.

Return the minimum possible value of the maximum integer of nums after performing any number of operations.

# EXAMPLE

    Input: nums = [3,7,1,6]
    Output: 5

Explanation:
One set of optimal operations is as follows:
1. Choose i = 1, and nums becomes [4,6,1,6].
2. Choose i = 3, and nums becomes [4,6,2,5].
3. Choose i = 1, and nums becomes [5,5,2,5].
   
The maximum integer of nums is 5. It can be shown that the maximum number cannot be less than 5.
Therefore, we return 5.

# BINARY SEARCH ON ANSWER APPROACH

How can we identify whether we can use Binary Search on this problem?

See, whenever you see any problem that asks us to "Minimize" or "Maximize" something, you have to try to see if there is monotonicity. 

For example, we are asked to "Minimize" the maximum value. It means, we have to make sure that we perform operations such that at the end, we have minimized the maximum value in the array to an extent that we cannot further minimize it.

	Suppose we take an example -> nums = [3,7,1,6]
	
	Here, as the example reveals, the output is 5. 
	
	5 means that if we take any index >= 1 and < n, and it is > 5, we can try to decrement it until it is == 5
	
	And the amount by which we decrement it is the same amount we have to use to increment the previous value
	
	We start with "7". Since 7 > 5. We decrement it by 2 so that 7 now becomes 7 - 2 = 5
	
	Since we decremented "7", that means, we have to increment "3" by the same amount. 
	
	So after first operation, the array becomes -> [5,5,1,6]
	
	Now, when we reach "6", again "6" > "5". So we decrement it by 1 to make it 5.
	
	And we also increment "1" to make it 2.
	
	Finally, array becomes [5,5,2,5]

Now, just think why cannot be any value less than "5" valid? What i we take "4" as the minimum value? Is it possible to convert all the values to be <= 4? Let's see.

	nums = [3,7,1,6]
	
	First, we have "7". We decrement it by 3 and increment previous "3" by "3". 

	nums = [6,4,1,6]
	
	Did you see what the issue is? Now, even though "3" was already a good value previously, since we added "3" more
	it now became > 4 which made it a bad value. So ofcourse "4" cannot be a valid value here.
	
	And since "4" is not valid, no value less than "4" is valid too. And that's the monotonicity.
	
	Similarly, if "5" was valid, then "6" or "7" or "8" or any value more than "5" is also a valid output. 
	
	But we want to minimize the valid value.
	
And since there is this monotonicity, it suggests we can apply Binary Search on this range of possible valid values. That's what we call -"**BINARY SEARCH ON ANSWER**".

Now think about what can be the range of valid possible minimum values? For test cases such as [10, 0] where the first element has the maximum value, there is no way we can minimize since decrement operation needs to be performed on indices >= 1 and < n. So this means, for any input, the upper limit is the maximum value in that input array.

And similarly, what can be the lower limit? That's what we are asked to find. We are asked to return the minimum possible valid value. And so, we can take the lower limit as "0". Since the nums[i] can be at least "0".

So now, we have this range [0, max(nums)] on which we have to apply Binary search. Each "mid" that we get is a possible valid minimum value. But we have to check if that's the case. IF yes, then as we saw above, all values greater than "mid" will be valid too. But if not, then all values less than "mid" will be invalid.

Now, continuing the example above - 

		nums = [3,7,1,6]
		
		When we considered min value as "4", we saw that it made a good value "3", bad 
		by incrementing it such that it became more than 4.
		
		This means, we cannot just blindly increment and decrement values.
		
		There must be some limit by which we can decrement one value and increment the other.
		
		For example in nums = [3,7,1,6], we can see that if we have min value as "5", then that means
		
		"3" cannot be incremented by any value > 2 because that would convert it to a bad value. 
		
		Hence, the increment limit is "2" here. And that means, we can decrement "7" by "2" only. 
		
		Not by any number > 2
	
		Hence, instead of trying to decrement a value and then increment the previous value, we can do the opposite.
		
		That is, try to see how much we can increment a value and then based on that 

		we can decrement the next value if it is more than the minimum we are trying to validate.
		

And that's why, in the "isValid()" method, I have a variable "buffer". It will check if current value is less than "x" then by what amount we can increment it such that it is still <= x. That will be our buffer.

Similarly, if some value is greater than "x", then the amount by which we can decrement it such that it is <= x should not be more than the buffer. We saw this when we considered "x" as "4" in nums = [3,7,1,6]. When it was "4", we saw that while buffer is only "1" for "3", we have to decrement "7" by "3" to make it <= 4. 

So if this is the case for any number, we can straight away return False as there is no way to make sure all values are <= x in that case.


