# PROBLEM STATEMENT

Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).


# EXAMPLE

    Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
    Output: 13
    Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13


# HEAP APPROACH - O(k) SPACE

The simplest approach includes using a MaxHeap and maintain its size as k. At the end, top of heap will have the kth smallest element.


# BINARY SEARCH APPROACH - O(1) SPACE

To do this problem in O(1) extra space, we can use Binary Search. This is one of those questions where we have to use the concept of "Binary Search on Answer" that is, we apply Binary search on a range of possible solutions. And this range is always in sorted order.

To find this range, we ask ourselves two questions - 

		1. What is the lower bound i.e., the smallest possible value for given input
		2. What is the upper bound i.e., the largest possible value for given input


Here, we have to find the Kth smallest element. Now just think. What is the lowest possible value of K for any input? It is 1 right? if K is 1 that just means we are asked for the first smallest or "THE" smallest element in matrix. That will always be the elemenat at Row = 0 and Col = 0.

And now think what is the largest possible K value? It is n^2. In that case, we are asked for "THE" largest element in matrix. Which will always be element at last row and last column. 

	So, the range of possible solutions is :
			matrix[0][[0] to matrix[n-1][n-1]


And since matrix is sorted, this range is also in a sorted order. Hence, we have to apply Binary Search on this range.

Now the question is, when we get any mid value, what do we check? How do we move to either left of mid or right of mid?

	matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
	
	Here, start = 1, end = 15
	
	So first mid we will get is 1 + 15/2 => 8
	
	Now, 8 is not even in the matrix so how to check? 
	
	Well, kth smallest element means that there are  k elements that are <= the given element (including itself)
	
	e.g. in matrix = [[1,5,9],[10,11,13],[12,13,15]] the 8th smallest is 13. That's because there are 8 elements before it (including itself) that are smaller or equal to it.
	
	So, here, we are not using mid as the solution. 
	
	We are using mid as a way to check on either left side or right side of it.
	
	If count of elements smaller than mid is < k, that means kth smallest cannot be on the left side of mid 
	
	So search on right of mid in that case
	
	Otherwise, if count of elements smaller than mid is >= k that means, the kth smallest can be on the left side of mid 
	
	So search on left of mid in that case
	
Finally, when the Binary Search ends, the left pointer will be pointing to the kth smallest element.