# PROBLEM STATEMENT

You are given two integer arrays persons and times. In an election, the ith vote was cast for persons[i] at time times[i].

For each query at a time t, find the person that was leading the election at time t. Votes cast at time t will count towards our query. In the case of a tie, the most recent vote (among tied candidates) wins.

Implement the TopVotedCandidate class:

    TopVotedCandidate(int[] persons, int[] times) Initializes the object with the persons and times arrays.
    int q(int t) Returns the number of the person that was leading the election at time t according to the mentioned rules.
 
 times is sorted in a strictly increasing order.

# BINARY SEARCH APPROACH

The biggest hint of Binary Search is in the constraints because we are given that 

			times is sorted in a strictly increasing order.
			
This means, if somehow we can figure out at a particular time, who was leading and keep this data in a list, that list will be sorted already based on the time. Since time is already sorted.

And so, we have to do two things - 

		1. Find who was leading at ith time and store that in a list
		2. Apply Binary Search on this list to find who was leading at a particular time

The first task can be done when we get the data itself i.e., when the TopVotedCandidate object is instantiated.
		
So we use a map to keep track of how many votes are casted to each person
		
And along with that, we also keep track of what is the maximum votes casted to any person
		
And based on these two, we can find who was leading at ith time.

	The rest is a simple Binary Search on the List to find the floor of the given time "t". 
	
	Floor means the smallest value that is <= "t"