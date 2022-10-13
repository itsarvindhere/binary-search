# PROBLEM STATMENT

In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.

# EXAMPLE

    Input: position = [1,2,3,4,7], m = 3
    Output: 3

Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.


# BINARY SEARCH ON ANSWER

There are so many problems similar to this and for all of those, the concept is the same - **BINARY SEARCH ON ANSWER.**

In this one too, we have to apply Binary Search on a sorted range of possible solutions. Because we know that - 

		If we can have a magnetic force of "x" between any two balls,
		that means any value less than "x" can also be a valid magnetic force value
		
Here, we first have to figure out the range of solutions. For that, the simplest way is to think of the smallest possible input and maximum possible input.

Here, what can be the smallest possible input? What if number of balls = number of positions? Which means, the minimum possible magnetic force between two values can be 1. 

And similalrly, what if number of balls is just 2, but there are a lot of positions? Then, we can place the two balls at the far ends of the sorted position array such that the difference between the two values is the maximum. 

	Hence, the Possible Range of solutions is 1 to (max - min) in sorted array
	
	Each value might be a possible candidate for solution. But if it is not, then any value after it is also not valid.
	In similar way, if it is valid, any value less than it is also valid
	
So we can use Binary Search such that we discard one half each time we find a valid or invalid value.

	If we get a valid value, we won't waste time checking for smaller values as they are all valid.
	If we get an invalid value, we won't waste time checking for larger values as they are all invalid.