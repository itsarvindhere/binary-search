# PROBLEM STATEMENT

Given an array arr of integers, check if there exist two indices i and j such that :

    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]

Constraints:

    2 <= arr.length <= 500
    -103 <= arr[i] <= 103
 

# EXAMPLE

    Input: arr = [10,2,5,3]
    Output: true

Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

# BRUTE FORCE APPROACH - O(N^2)

According to the constraints, the list length will be at most 500. So we can write a Brute Force solution and that will be accepted.

# BINARY SEARCH APPROACH - O(NLogN)

Can we do better than O(N^2)?

For every element, we are looking at every other element to see if it is a double. We have to do this because the list is not sorted so it is possible that for any element, its double is before it or after it in the list.

But if the list was sorted, then we can apply Binary Search because then, if the mid element is not double, then either it will be more than double or less than double. And based on that, we can either discard the left half or the right half. This will bring the complexity down to O(NLogN)

# SET APPROACH - O(N)

Is there a way to solve this problem in just one loop? Yes! See, we know that if the list is not sorted, then for any element, its double can either be on its left or its right. For a moment, lets forget that it is on the right. If the double of an element is on its left, then is there a way to check if the double exists on left in O(1) time? That's where we can use a Set.

As we loop through every element, we also keep checking if we have already came across the double of that element before in the array. If yes, we got a pair. If not, we can put that element in set and move to the next iteration. 

But there is one issue.

Lets take an example - 

			5 ,13, 10 ,6
			
			Here, when we start the loop, we put 5 and 13 in the set as their doubles are not in set yet
			
			So, set = (5, 13)
			
			Now when we come to 10. We check if its double is in the set. We don't find it so we move on.
			
			And at the end, we return False.
			
			But if you see, the double of 5 is 10 so there is a valid pair which means we should return True.
			
			And now you can see that we not only need to check for the double in set but also for the half.
			
			So, for every element, we check if its half exists in set or if its double exists in set.
			
			In both cases, we have a valid pair.
			
And that's the whole idea of this approach.

Do note that this approach will use extra space, something the previous two solutions don't.