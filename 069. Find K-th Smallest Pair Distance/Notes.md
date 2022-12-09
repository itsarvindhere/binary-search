# PROBLEM STATEMENT

The distance of a pair of integers a and b is defined as the absolute difference between a and b.

Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.

# EXAMPLE

    Input: nums = [1,3,1], k = 1
    Output: 0

Explanation: Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.

# BINARY SEARCH ON ANSWER APPROACH

This is one of the problems where we have to Binary Search the range of possible answers. We can apply Binary Search on this range because it will be in a sorted order. Let me explain.

We want the "Kth Smallest Distance". So, why not first define what can be the range of distances for any given input. What can be the smallest possible distance between two elements? It can be 0 right? Because nums[i] can be at least "0". So if we have two "0" in an array, they will pair up and distance will be 0.

So this will be our lower bound.

And similarly, what can be the largest possible distance? It can be 10^6. Because nums[i] can be up to 10^6. So, suppose if we have "0" and "10^6" in any array. In that case, the distance between them will be 10^6. And no distance can be greater than this for any given input.

To make it even simpler, we can take upper bound as simply the maximum element in any given input. because no distance can be bigger than max element.

So, this will be our upper bound.

And so, we got this range [0, max(nums)] in which each value means "distance". And since we want the "Kth" smallest distance, it means, whatever "mid" we get in each Binary Search, we have to then check how many pairs are there that have distance <= mid. If we have K or more pairs with distance <= mid, it simply means either "mid" is the kth smallest distance or the kth smallest distance is on the left side of "mid".

# **HOW TO FIND NUMBER OF PAIRS WITH DISTANCE <= X?**
## **METHOD 1 - USING BINARY SEARCH ITSELF**

Well, the biggest challenge is to find how many pairs are there with disance <= x. Only if there are K or more pairs that have distance <= "mid" then our "mid" value is valid. 

Now, to find the count, we have to Sort the array. Why?

Because, if array is sorted, then for any element, all we want to find is the rightmost element that will give distance <= "mid". Because we know all elements in between will also pair up to give distance <= mid only in that case. And we can easily count the number of pairs in between if we get the rightmost index of that element.

	e.g. take an example nums = [1,2,3,4,5,6]
	
	Suppose, we want to count how many pairs have distance <= 4
	
	Let's start with element 1 at index 0.
	
	Now, since this array is sorted, what is the biggest element that can pair with "1" to give distance of <= 4?
	
	It is "5". 
	
	Since "1" is at index 0 and "5" is at index 4. It means, there are in total 4 - 0  = 4 pairs  that have distance <= 4
	
	And indeed there are 4 pairs -> (1,2), (1,3), (1,4), (1,5)
	
	And similarly, we can find for every element, how many pairs will give distance <= "mid"
	
And now, all we want to return is whether there are K or more pairs with distance <= mid.
## **METHOD 2 - USING SLIDING WINDOW**

Wait a minute. How did sliding window come into picture here?

We want to count how many pairs are there with distance <= "mid". And since Array is sorted, we can use Sliding Window. How?


	e.g. take an example nums = [1,2,3,4,5,6]
	
	Suppose, we want to count how many pairs have distance <= 4
	
	See, if we have a window [1,2,3,4] then we see this is a valid window 
	because the distance between the max and smallest element is still <= 4
	
	This also means, there are "3" pairs in total - (1,2), (1,3) and (1,4). So they are simply (index of 4 - index of 1)
	That is, the (last element's index in window - first element's index in window)
	
	Now, if from 1 to 4, we have a valid window. Doesn't it mean from 2 to 4 as well the window is valid? 
		
	All we have to ensure is that the smallest and largest window element is having distance <= x and window will be valid
	
	And so, all we will do is, if the window is valid, just add the count. 
	
	But if it is not, we know that we need to shrink it from left side.
	
And in this way, the time complexity of our Helper method will be O(N), as compared to O(NLogN) in case of above approach.

## **METHOD 3 - BACK TO BINARY SEARCH BUT OPTIMIZED**

We can optimize the Binary Search Method #1 even further after we got to know that for any new element, all the elements till the last valid rightmost index will be valid too. So, we can make the Binary Search even better by searching after the previous rightmost valid index.