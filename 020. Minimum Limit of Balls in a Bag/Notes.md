# PROBLEM STATEMENT

You are given an integer array nums where the ith bag contains nums[i] balls. You are also given an integer maxOperations.

You can perform the following operation at most maxOperations times:

Take any bag of balls and divide it into two new bags with a positive number of balls.
For example, a bag of 5 balls can become two new bags of 1 and 4 balls, or two new bags of 2 and 3 balls.
Your penalty is the maximum number of balls in a bag. You want to minimize your penalty after the operations.

Return the minimum possible penalty after performing the operations.

# EXAMPLE

    Input: nums = [9], maxOperations = 2
    Output: 3

Explanation: 
- Divide the bag with 9 balls into two bags of sizes 6 and 3. [9] -> [6,3].
- Divide the bag with 6 balls into two bags of sizes 3 and 3. [6,3] -> [3,3,3].
The bag with the most number of balls has 3 balls, so your penalty is 3 and you should return 3.


# BINARY SEARCH ON ANSWER APPROACH

We can use the Concept of "Binary Search on Answer" to solve this problem.

We want to find the minimum penalty value. Now think about what is the range of valid penalty values? A penalty is nothing but number of balls in a bag.

So, what is the minimum balls a bag in given array can have? It is 1, right? Because that's what the constraints suggest.
And similalrly, what is the maximum balls a bag in an array can have, it is the maximum value in the given array. Because each value in given array means number of balls in that bag. So the maximum value is the maximum balls in any bag in that array.

And so, we got a range 1 to max(array)

And this range has all the possible solutions. Some are valid, some are not. And if some value is not valid, then any value less than it will also be invalid. And vice versa. So this means, we can discard one half each time we find a valid of invalid value. Which means we can apply Binary search on this range.

			nums = [2,4,8,2], maxOperations = 4
			
			Range is from 1 to 8
			
			So, start = 1, end = 8
			
			We get mid = 4
			
			So, how can we say if 4 is a valid penalty value? 
			
			We can say that if the maximum value in the array is 4 after performing at most maxOperations
			
So, we can have a helper method which we use to see how many operations are needed to make sure 4 is the largest value in array.	
That is, every value is <= 4

		nums = [2,4,8,2], maxOperations = 4
		
		We see that only 8 is the value that is greater than 4. 
		
		So we have to use some operations to divide it such that the maximum of two values that we get after dividing it is 4.
		
		This means, we cannot divide 8 into 5 and 3. Or, 6 and 2. 
		
		In one step, we need to find how many operations it would take to convert 8 into two values such that max of two values is 4.
		
		How can we do that? 
		
		Just by looking we know that it would take one operation to convert 8 into [4,4]
		
		What if we had 9? 
		
		In that case, it would need two operations because in one go, we would've done -> [4,5] 
		And in another operation, we would've done -> [4,1,3]
		
		What if we had 7? We would need 1 operation to convert it to [4,3]
		
		So, if penalty = 4, the pattern is like
		
		For 5, we need 1 operation
		For 6, we need 1 operation
		For 7, we need 1 operation
		For 8, we need 1 operation
		For 9, we need 2 operations
		For 10, we need 2 operations
		For 11, we need 2 operations
		For 12, we need 2 operations
		For 13, we need 3 operations
		
Notice the pattern? We can generalize this pattern as -
		
		
	We can see that for any value that is divisible by "penalty", we need (value/ penalty) - 1 operations.
	Whereas, for any value that is not divisible by "penalty", we need (value/penalty) operations
	
And for this reason, in the Helper function, we check if a value is divisible by penalty or not. If yes, decrement the operation count by 1.