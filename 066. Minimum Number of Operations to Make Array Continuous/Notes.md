# PROBLEM STATEMENT

You are given an integer array nums. In one operation, you can replace any element in nums with any integer.

nums is considered continuous if both of the following conditions are fulfilled:

 1. All elements in nums are unique.
 2. The difference between the maximum element and the minimum element in nums equals nums.length - 1.
   
For example, nums = [4, 2, 5, 3] is continuous, but nums = [1, 2, 3, 5, 6] is not continuous.

Return the minimum number of operations to make nums continuous.

# EXAMPLE

    Input: nums = [1,2,3,5,6]
    Output: 1

Explanation: One possible solution is to change the last element to 4.
The resulting array is [1,2,3,5,4], which is continuous.

# BASIC IDEA OF THE SOLUTION 

See, we want to convert the array into a "continuous" array such that, the final array has no duplicate elements and also, the difference between maximum and minimum element is "length - 1"

Now if you think, it just means, that if "x" is the starting element in the final continuous array, then the maximum element should be "x + n - 1". Also, we are not asked to return the continous array. Instead, we are asked to find how many elements to replace.

Since we want to minimize the replacements, it means, from the original input array, we should be able to reuse the maximum number of elements in our final array. Because, if we maximize the number of elements we reuse, we will minimize the number of elements we replace. That's the main idea of all the approaches below.

Since final array should not have any duplicates, this means, once we use an element, we will not be reusing same element again. And so, it means, we can straight off remove the duplicates first. Set will come handy in this case.

Now, the minimum in our continuous array can be any element from original array. For example, if we are given [1,2,3,5,6] then what can be the continuous array if we make each element as minimum - 

		If "1" is the minimum -> [1,2,3,4,5]
		If "2" is the minimum -> [2,3,4,5,6]
		If "3" is the minimum -> [3,4,5,6,7]
		If "5" is the minimum -> [5,6,7,8,9]
		If "6" is the minimum -> [6,7,8,9,10]

So, in which case we have to make the minimum number of replacements? We can use the set that we created above for that because lookup is O(1) operation.

If "X" is the minimum element in the final array, we know "X + N - 1" will be the maximum. So, we can check how many elements from "X" to "X + N - 1" are present in the set. If all are present, we basically do not need to make any replacements and the array is already continuous.

# BRUTE FORCE APPROACH

The Brute Force approach is pretty straight forward. Consider each element as "minimum" and check how many elements are present in the set in the range [num, num + n - 1]. That will be our number of elements we can reuse.

Find the minimum replacements and return that.

But this approach is not efficient and will fail for large test cases.

# BINARY SEARCH APPROACH

How can we use Binary Search?

We also know that if we "Maximize" the number of elements we can reuse, then the replacements will be "Minimized". 

So, for each element, if we consider it as the minimum element, then all that we want to find is how many elements are there in the range [element, element + n - 1] in the input array. We can reuse all of them, right? And so, if we sort our array, then we can use Binary search to find just that.

And that's the idea of this approach. 

Take each element, consider it as minimum, and then find how many elements are already present in the array that are <= element + n - 1. 

One thing that's important is that, in the "start" and "end", the length of array is the length of the new array that we created after removing duplicates. But, the "n" is the length of array originally. Because our continuous array needs to be of length "n". 


# SLIDING WINDOW

Well, there is no need of Binary Search as well if you think a bit.

Because basically, after sorting, all that we are looking for is what is the longest subarray that starts with element "X" and the maximum element in this subarray does not exceed "X + N - 1".  Because all the elements in this subarray will be reused if "X" is the minimum element in final continuous array. 

And well, here, we can make use of Sliding Window approach because we are dealing with subarray here and we want the Maximum length subarray such that the maximum element in the subarray is <= (minimum element + n - 1)
 