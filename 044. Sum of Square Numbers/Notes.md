# PROBLEM STATEMENT

Given a non-negative integer c, decide whether there're two integers a and b such that a^2 + b^2 = c.

Constraints:

    0 <= c <= 2^31 - 1


# EXAMPLE

    Input: c = 5
    Output: true
    Explanation: 1 * 1 + 2 * 2 = 5

## **1. BRUTE FORCE APPROACH - O(sqrt(c)^2) ➜ O(c)**

The constraint says that "c" can be as large as "2^31 - 1" which means even an O(c) solution will give TLE. This is a hint that we need to write a solution that is better than even O(c) solution. 

Anyways, the idea is that since we are asked for two numbers "a" and "b" such that - 

		a^2 + b^2 = c
		
It means, "a" and "b" should be in the range 0 to sqrt(c). And that's the range in which we can find two values, if they exist.

So, in Brute Force approach, for every possible value of "a", we go through every possible value of "b". Since both loops run from 0 to sqrt(c), the time complexity is O(sqrt(c) ^ 2) or O(c)
		
		
## **2. BINARY SEARCH APPROACH #1 - O(sqrt(c) * log(sqrt(c)))**

As discussed above, the range for both "a" and "b" is from 0 to sqrt(c). This range is also in a sorted order. This means, instead of linear scan, we can use Binary Search in the inner loop such that we search for a valid value of "b" that satisfies the equation.

In each iteration of Binary Search, we will get a new "mid" or in other words, a new value of "b". And we just need to check if the equation "a^2 + b^2" gives us "c" or not. If it does, then we can straight away return "True".

But if it does not, there are two cases - 

	1. "a^2 + b^2" is more than c
	2. "a^2 + b^2" is less than c

If it is more than "c", then that means the value of "b" is more than required. Because "a" and "c" will remain the same for every iteration of inner loop. But only "b" can increase or decrease. This means, the value of equation being more or less than "c" depends on "b" or "mid". Hence, we search on left side of "mid".

If the value is less than "c", that means value of "b" needs to be increased, hence we search on right side of mid.

## **3. BINARY SEARCH APPROACH #2 - O(sqrt(c) * log(sqrt(c)))**

Another way to apply Binary search is to directly search for the value of "b" that will satisfy the equation. 

We are given that - 
		
			a^2 + b^2 = c
		or, b^2 = c - a^2
		or, b = sqrt(c - a^2)
		
Hence, all we need to Binary Search is this value of "b" in the range 0 to sqrt(c).

## **4. TWO POINTERS APPROACH - O(sqrt(c))**

The most efficient way to solve this problem is using Two Pointer approach that will have a time complexity of O(sqrt(c)).

We know that both values are in range 0 to sqrt(c)

So what we can do is initially, set "a" as the smallest value in this range i.e., 0
And set "b" as the largest value i.e., sqrt(c)

And now, while a is <= b, we will check the equation. If it is satisfies, we found a pair.

But, if "a^2 + b^2" is more than "c", that means, either "a" is larger than what we need or "b" is larger than what we need. And it makes sense to decrease "b" in this case because "b" is always the larger of the two.

Similarly, if "a^2 + b^2" is less than "c", that means, either "a" is smaller than what we need or "b" is smaller than what we need. And it makes sense to increase "a" in this case because "a" is always the smaller of the two.

