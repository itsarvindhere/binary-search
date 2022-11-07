# PROBLEM STATEMENT

Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

    0 <= i, j < nums.length
    i != j
    nums[i] - nums[j] == k

Notice that |val| denotes the absolute value of val.

    1 <= nums.length <= 104

# EXAMPLE

    Input: nums = [3,1,4,1,5], k = 2
    Output: 2

Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.


# BRUTE FORCE - O(N^2)

The Brute Force approach is pretty straightforward. We go through each number and for each number, we traverse the list from beginning to find a suitable number to pair with. Since we want only the unique pairs, we will use a Set to keep track of first element of each pair. Since we are not checking "absolute" difference, the condition "nums[i] - nums[j] == k" will only be true when nums[i] >= nums[j].

So we can simply put the nums[i] in the set each time we find the pair so that the next time we find the same pair, we ignore that.

In the end, we will return the size of the set as the size of set = number of unique pairs.

This solution will fail for large test cases and you will get TLE. But from here, we can start thinking of an Optimized Solution.

# BINARY SEARCH - O(NLogN)

The reason why the Brute Force approach fails is because for each number, we have to traverse the list again from the beginning. What if the list was in a sorted order? Suppose we sort the list in increasing order. In that case, for each first number, we need to find a second number that is larger than it that is, it is present on the right side of it. And also, the difference of second - first should give k.

You can think of this "second number" that we will search for as "nums[i]". I also made sure to name the loop variables in the same way in the code.

    We we want a pair such that nums[i] - nums[j] == k

    We can rewrite this as -> nums[i] = k + nums[j]

    It means, for every nums[j], we want to search for a number nums[i] that is equal to -> k + nums[j]


And well, that's the basic idea of our Binary Search approach. Since our array is now in a sorted order, there is no need to traverse the array from the beginning each time.


# DICTIONARY - O(N)

Finally, we have the O(N) solution which is using a Dictionary. Now, all that we want is for each number, we are looking for a second number such that second number = k + first number.

If we have a dictionary that has all the elements and their counts, we know we can search for this second number in O(1) time, right? In that case, there is no need for Binary search which will reduce the complexity from O(NLogN) to O(N).

To ensure that we only cover uniques, we can loop over the dictionary keys, instead of the elements of array. This will ensure an element can be the "first number" only once, no matter if it appears multiple times.


    Consider this example -> [1,1,1,1] and k = 0

    our dictionary is like - {1 : 4}

    If we loop over this array then we will have four iterations and in each iteration, we have "1" as first number

    And so we will get multiple pairs like (1,1), (1,1) and (1,1)

    But as we have to only take unique pairs, we will have to use a set here again.

    But if we loop over the keys of dictionary, then every element can be the first number of the pair exactly once.

