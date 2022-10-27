# PROBLEM STATEMENT

There are n persons on a social media website. You are given an integer array ages where ages[i] is the age of the ith person.

A Person x will not send a friend request to a person y (x != y) if any of the following conditions is true:

    age[y] <= 0.5 * age[x] + 7
    age[y] > age[x]
    age[y] > 100 && age[x] < 100

Otherwise, x will send a friend request to y.

Note that if x sends a request to y, y will not necessarily send a request to x. Also, a person will not send a friend request to themself.

Return the total number of friend requests made.

 
# EXAMPLE

    Input: ages = [16,17,18]
    Output: 2
    Explanation: Friend requests are made 17 -> 16, 18 -> 17.

# BRUTE FORCE APPROACH - O(N^2)

The Brute Force Solution is pretty simple. For every age, find every other age to which friend request can be sent.

    It is given that, "x" cannot send a friend request to "y" if - 
	
		age[y] <= 0.5 * age[x] + 7
		age[y] > age[x]
		age[y] > 100 && age[x] < 100
		
We can rewrite these conditions such that,

	"x" can send a friend request to "y" if - 
	
		age[y] > 0.5 * age[x] + 7
		age[y] <= age[x]
		
We do not need to care about third condition as that will be covered in the above two because in the above two, we are checking that age of "y" should be at most equal to age of "x", not more than that. 


# BINARY SEARCH APPROACH - O(NLogN)

Take a look at the conditions carefully -

		age[y] > 0.5 * age[x] + 7
		age[y] <= age[x]
		

This means, the range of valid values of age[y] for any age[x] is from -> 0.5 * age[x] + 7 to age[x]

Hence, for any age[x], we can try to find the smallest possible value in the array that is  > 0.5 * age[x] + 7
And also, we can try to find the largest possible value that is =<= age[x]

And then, the number of values in between will be the number of friend requests that x can send.

We can do that using Binary Search but for that, we also need to sort the list first.

# OPTIMIZED BINARY SEARCH APPROACH - O(NLogN)

Since ages may be duplicate, why do the same process for an age if we have done it before? 
