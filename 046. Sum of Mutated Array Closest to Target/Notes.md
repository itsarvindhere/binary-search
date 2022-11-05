# PROBLEM STATEMENT

Given an integer array arr and a target value target, return the integer value such that when we change all the integers larger than value in the given array to be equal to value, the sum of the array gets as close as possible (in absolute difference) to target.

In case of a tie, return the minimum such integer.

Notice that the answer is not neccesarilly a number from arr.

# EXAMPLE

    Input: arr = [4,9,3], target = 10
    Output: 3

Explanation: When using 3 arr converts to [3, 3, 3] which sums 9 and that's the optimal answer.

# BINARY SEARCH APPROACH

We are asked for a "value" such that sum of the array after replacing all elements bigger than "value" by "value" is closest to the "target".

Now think about it. What can be the closest sum? It can be the "sum" that is equal to "target", right? Because in that case, the difference will be 0 which is the smallest possible absolute difference.

	This is something you will see in test case arr = [2,3,5], target = 10
	
	Because here, the sum of array is already equal to 10. So there is no need to replace any number.
	
	In other words, in this case, the required value is "5" because only if value is "5" we will get sum = 10
	
	If value is more than "5", then too we will get sum = 10 but we are asked for minimum value in case of tie.


To understand it better, here is a graph of the "sum" and "value" - 

![image](https://assets.leetcode.com/users/images/22576c83-8cdf-44c3-b3eb-e1f22924bb57_1667635289.4486818.png)


If you see, when value is 1, we get sum = 3 because we have to replace all values in array by 1 as all are greater. 
But when value is 2, we get a higher sum. So absolute difference will be smaller than before. 
And so on when we reach value = 5, in that case, sum will be 10 which is the same as target. So this is the required value here.

***HENCE, THE MAIN IDEA IS TO TRY TO FIND THE CLOSEST SUM, THAT IS, THE SUM THAT IS EQUAL TO TARGET!***

Even if there exists no such value for a test case where sum of array becomes equal to target, then we will get two values that will give us two closest sums.

Take a look at this graph as an example - 

![image](https://assets.leetcode.com/users/images/4f01b43a-d067-427d-a8d3-f5ab2ab38a86_1667635027.957436.png)

As we can see, at value 4, the sum will be 11. And since target = 10, absolute difference = 1
But at value = 3, sum will be 9. And here as well, absolute difference is 1.

So we have a tie here. Hence, in this case, we will go for the minimum of two values, which is 3.

Hence, the basic idea of the Binary Search approach is that we try to find a value that results in "sum == target". If we can find such a value, we can simply return it. If the sum is less than target, we want a bigger sum hence we move to right side of mid. But if sum is greater than target, we want a smaller sum hence we move to left side of mid.

After binary search ends, if we were not able to find a value that results in "sum == target", then  we will get two values that will result in the closest absolute difference that is, "start" and "end".

And we have to choose one of them as the output, depending on whether absolute difference of one is smaller than the other.
