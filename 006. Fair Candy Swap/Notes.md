# PROBLEM STATEMENT

Alice and Bob have a different total number of candies. You are given two integer arrays aliceSizes and bobSizes where aliceSizes[i] is the number of candies of the ith box of candy that Alice has and bobSizes[j] is the number of candies of the jth box of candy that Bob has.

Since they are friends, they would like to exchange one candy box each so that after the exchange, they both have the same total amount of candy. The total amount of candy a person has is the sum of the number of candies in each box they have.

Return an integer array answer where answer[0] is the number of candies in the box that Alice must exchange, and answer[1] is the number of candies in the box that Bob must exchange. If there are multiple answers, you may return any one of them. It is guaranteed that at least one answer exists.


# EXAMPLE

    Input: aliceSizes = [1,2], bobSizes = [2,3]
    Output: [1,2]


# APPROACH

There are various ways to solve this problem. Before talking about those three ways, lets get a basic idea of how we can find the required output.

So, we are given two arrays and each value indicates candies in a box. We want to swap candies such that both alice and bob have same amount of candies. 

	What that means is at the end, both should have (sum of aliceSizes initially + sum of bobSizes initially) / 2 candies.
	
	aliceSizes = [1,2], bobSizes = [2,3]
	sum of aliceSizes = 3
	sum of bobSizes = 5
	Total sum = 8
	
	So at the end, both should have equal candies i.e., 4 candies.
	
	
Hence, what we can do is for each value in alice, try to see if we can find any value from bob to swap. How to check if we can swap?

Lets say we take value = 1 from aliceSizes and we want to see if we can swap it with any other value.

Since Alice tries swapping 1, that means, she might get some new value in place of 1. And so, that new value will then be added to the initialSum and 1 will be taken out as she is giving away 1 to bob.

In simple words, she is giving 1 sized box and receiving 2 sized box so that's why the final sum will be 2 + (initialSum - 1)

And since we know that at the end, finalSum should be 4 for both, all we need to check is whether 2 + (initialSum - 1) == 4 or not.

This will be condition to check if we can swap two values. So the check can be generalised as  - 

	
				val from bobSizes + (initial sum of aliceSizes - val from aliceSizes) == (sum of aliceSizes + sum of  bobSizes)/2

## **1. BRUTE FORCE - O(n^2) Time Complexity and O(1) Space**

This will give TLE because the size of the list can be up to 10^4 so it will fail for large inputs. No need to code but understand that in this one, we will have two nested loops and for each aliceVal, we go through each value in bobSizes array. Then apply above condition to see if any bobVal makes this condition true.

## **2. BINARY SEARCH - O(nlogn) Time Complexity and O(1) Space**

One way to optimize our solution is to use Binary Search instead of linear search.

Because for any value in aliceSize, if any value is invalid in bobSizes, then all the values less than or equal to mid value will also be invalid (I will explain later how to check that).

So we can avoid again checking for values that we already know are invalid.

So we will have to first sort the given array. And then, for each value in aliceSizes array, apply binarySearch on bobSizes and again check for the same condition as in case of Brute Force Solution.

We will check the condition for mid element each time.

Now comes the question -> Which way to move if mid does not satisfy the condition?

Just think about this -> In binary search, aliceVal will be constant, and sum of aliceSizes will be constant. The only value that will change during Binary Seach is the bobVal. So we can have three situations - 

	bobVal + constant == half => We found values to swap
	bobVal + constant < half => bobVal is small so go for a larger bobVal
	bobVal + constant > half => bobVal is large so go for a smaller bobVal
	
And that's how we can go either to left of mid or right of mid.

## **3. SET - O(n) Time Complexity and O(n) Space**

Finally, we come to the O(n) time solution for this problem. For this, we have to use extra space because we will be using a Set. 

Lets go back to the condition - 

		bobVal + (aliceSizes sum - aliceVal) == half
		
		
Instead of using both bobVal and aliceVal, why cannot we use a set to get an aliceVal for a particular bobVal. Because we know searching in a set is O(1) operation.

To find aliceVal from above condition, we can rearrange it as - 
		
		aliceVal = bobVal + (aliceSizes sum - half)

If we create a set of aliceSizes, then for any bobVal, all we need to check is if the set has any value = bobVal + (aliceSizes sum - half)