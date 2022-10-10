# PROBLEM STATEMENT

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

# EXAMPLE

    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# BRUTE FORCE APPROACH - O(N^2)

The simplest way is - Try to find a number for every number such that both add up to target.

But ofcourse, this is the least efficient approach because we will have two nested loops and in worst case, we will have O(N^2) Time complexity. And since length of numbers list can be up to 3 * 10^4, this solution will fail for large arrays and you will get TLE.

But the advantage of writing a right Brute Force solution is that you can get an idea of how to optimize it.

# BINARY SEARCH APPROACH - O(NLogN)

We see that the given array is already sorted. This means, we can use Binary Seach in place of linear search. In Brute Force approach, for every number, we do a linear scan to find second number. But since array is sorted, why not use Binary Search for that?

For every number, we want to find another number such that -

	num1 + num2 = target
	
If we know num1 and we know target, we can find num2 easily, right?

	num2 = target - num1
	
So we have to Binary Search for a number that is equal to  target - num1

And one thing to note is that, it is given that in the result array [index1, index2], index1 is less than index2. So this means, for any number, we have to Binary search for a number that is >= that number. In other words, the range of Binary search starts from the index just after the index of num1. Only then we can be sure that index1 < index2.

And for the same reason, we checked if i2 > i1 in the above Brute Force solution.

Now, when we get a number which is less than target - num1 it basically means that we have to find a larger number and for that, we have to search on right side of mid. Otherwise, vice versa.

# TWO POINTERS APPROACH - O(N)

The best way to solve this problem is using a Two Pointer approach. Because this approach has time complexity of O(N). Since array is already sorted, this means, the first element is the smallest in the array and the last is the largest. 

So we keep two pointers, one initially pointing to first index and the other to last index.

And we check if they both add up to target. If not, there are two cases - 

		1. Their sum > target
		2. Their sum < target

If their sum > target, that means, one of the values is larger than we need. So that means, the right pointer points to a value that is larger than what we need. So we decrement the right pointer to get a smaller value.

If their sum < target, that means, one of the values is smaller than we need. So that means, the left pointer points to a value that is smaller than what we need. So we increment the left pointer to get a bigger value.