# PROBLEM STATEMENT
You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).

# EXAMPLE

    Input
    ["Solution","pickIndex"]
    [[[1]],[]]
    Output
    [null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.


# APPROACH

	Suppose we have an array -> [1,3,2]

	As we are given, each number's probability of being chosen is weight/sum 
	
	This means, 
	
		For index 0, probability is 1/6
		For index 1, it is 3/6
		For index 2, it is 2/6
		
	One way to represent the probabilities of each index are - 
	
		[0,1,1,1,2,2]
		
	Since index 0 has 1/6 probability, it is only occuring once in this array.
	But since index 1 has 3/6 probability, it occurs 3 times.
	And finally index 2 has probability 2/6 so it occurs 2 times.
	
	But this won't be efficient. We can represent probabilities in one more way. That's using a number line.
	

![image](https://assets.leetcode.com/users/images/0d11112b-110d-4bb7-a830-13a33400d191_1667545512.045621.png)
		
We can represent this probability on a number line such that the length of each portion represents the weight at each index.

Now, each value represents a boundary for any index. For for index = 0, range is [0,1]. For index = 2, range is [1,4] (excluding 1 since 1 is where index = 0 ends). And so on...

And as we can see, the values on number line are nothing but the values of the prefix sum array of the given array. 

Okay. But how does this helps in solving this problem?

Now, all that's left is to generate a random number and then we need to return the correct index value. Suppose we generate a number  = 2. As we can see on number line, 2 is between 1 and 4 which is the range of index = 2. Hence, in that case, we need to return 2. 

This also means that the random number that we have to generate is between 1 to the total sum of the array given as input.

And whatever number we get, we need to then find what is the closest index to that number. For that, we can use Binary Search since the prefix sum array is always in a sorted order as all numbers are positive. We will return the "start" value if the random value is not present in prefix sum array because we want the closest element to the right side of any random value.

	Suppose we have a prefix sum array as [1,3,6]
	
	If random number generated is 2, then it is closer to both 1 and 3 
	
	but we have to go with 3 as the closest number since the probability is higher on right side. 
	
	That's why we did not return "end" but rather the "start" value after Binary Search.

*NOTE that in the above image, the number line starts from 0. It is just to show each portion for each weight. But in code, we will calculate prefix sum such that prefix sum array is of the same size as the input array. So there won't be 0 at the first index of prefix sum array.*

	Example: [1,3,2]
	
	prefix sum array = [1,4,6]
	
	And now,  we generate a random number between 1 to 6. Suppose we get 3.
	
	We have to now do binary search for the closest value in the prefix sum array.
	
	Whatever closest value we get, we return the index of it at the end.
	
	It is also possible the random number we generate is a value present in prefix sum array. 
	
	For example, if we get random number as 4 then we will see that at index = 1, we have value = 4 in prefix sum array.
	
	So in that case, we will straight away return the index. 