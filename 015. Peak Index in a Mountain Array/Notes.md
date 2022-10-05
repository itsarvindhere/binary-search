# PROBLEM STATEMENT

An array arr a mountain if the following properties hold:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
        Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.

# BRUTE FORCE - O(N)

The Brute Force approach is pretty straightforward. Just check for each index, whether its left and right elements are smaller than it.

If yes, then it is the peak.

# BINARY SEARCH - O(LogN)

Instead of checking each index, starting from the first, we can use Binary Search for this problem so the time complexity will be O(LogN) as asked by the problem.

## **How can we use Binary Search in this problem? Is the array sorted?**
	
It is guaranteed in this problem that the input array will always be a valid mountain array which means it will always have one peak index. You can verify that by trying to input any array which does not have any peak or has multiple peaks. It will give you error while running that test case saying - "*arr is not a mountain array*"

What that means is that till the peak, the array is in increasing order. And after the peak, array is in decreasing order. So yes, it is sorted before and after the peak element.


## **Approach**

Well, in Binary search, we check the mid element. And if mid satisfies some particular condition, then we return or do something else. And if it does not, we either discard the left side or right side of mid.

	So lets say we found that mid is not the peak index. Then which way we move?

	The answer is - We move that way where we have more chance of finding a peak index. 
	
	
Lets understand using an Example.

		[0,5,10,2]
		
		Initially, we get mid as the 1st index. But at index = 1, we see that while 5 is greater than 0, it is not greater than 10.
		
		What that means? 
		
		It means, while 5 is not the peak, 10 can be the peak 
		
		Because it is already bigger than its left element so it may have a smaller element on its right.
		
		Even if 10 has a bigger element on its right, that means we still have a better chance to find peak on the right side only.
		
		Similarly, 0 can never be the peak because since 5 is already greater than 0, why care about what is on the left of 0. 
		
		So we move towards the right of mid if the mid element is smaller than mid + 1 element. And vice versa.
		
	
## **How does going to right of mid or left of mid guarantee the peak on that side?**

	See, if you are at mid and see that the element on left side is smaller but on the right, the element is bigger. 

	This basically means, that you are going towards the peak if you move to right side of mid. 

	Similarly, if you are at mid and element on left is bigger.

	That means you already moved past the peak so to find the peak, we need to go back which means towards the left side of mid.