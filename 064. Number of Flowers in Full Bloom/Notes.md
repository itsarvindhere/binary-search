# PROBLEM STATEMENT

You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array persons of size n, where persons[i] is the time that the ith person will arrive to see the flowers.

Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.

# EXAMPLE

    Input: flowers = [[1,6],[3,7],[9,12],[4,13]], persons = [2,3,7,11]
    Output: [1,2,2,2]
    
Explanation: The figure above shows the times when the flowers are in full bloom and when the people arrive.
For each person, we return the number of flowers in full bloom during their arrival.



## **1. BRUTE FORCE APPROACH - TLE**

The Brute Force approach is quite straightforward. For each person, we want to count how many flowers are there that are in full bloom at that person's arriving time. We know that a flower is in full bloom during [start, end]. 

So that means, for a person's arriving time, a particular flower will be in full bloom if and only if it starts blooming at arriving time or has already started blooming before person arrives. And also, that flower stops blooming when person arrives or will stop blooming after the person arrives.

But here, for each person, we have to traverse the whole list of flowers again and again so for large test cases, it will give TLE.  But from here, we can start thinking of a better approach.

## **2. BINARY SEARCH APPROACH**

How can we avoid traversing the whole list of flowers for each person? In simple words if we describe this problem, then for a particular time, we want to find how many flowers are blooming. So we say that at a particular time - 

	Number of Flowers Blooming at time "t" = Number of flowers that have started blooming at or before time "t" - Number of Flowers that have stopped blooming before time "t"
	
	
	Example: flowers = [[1,6],[3,7],[9,12],[4,13]], persons = [2,3,7,11]
	
	If a person[2] arrives at time = 7. Then we see that - 
	
	flower[0] started blooming before "7" because for it, start = 1 and 1 <= 7
	flower[1] started blooming before "7" because for it, start = 3 and 3 <= 7
	flower[2] started blooming after "7" because for it, start = 9 and 9 is not <= 7
	flower[3] started blooming before "7" because for it, start = 4 and 4 <= 7
	
	Hence, Number of Flowers that have started blooming at or before time "t" => 3
	
	Similarly,
	
	flower[0] stopped blooming before "7" because for it, end = 6 and 6 < 7
	flower[1] did not stop blooming before "7" because for it, end = 7 and 7 is not < 7
	flower[2] did not stop blooming before "7" because for it, end = 12 and 12 is not < 7
	flower[2] did not stop blooming before "7" because for it, end = 13 and 13 is not < 7
	
	Hence, Number of flowers that have stopped blooming already => 1
	
	This means, 
	
	At time = "7", we have => 3 - 1 => 2 flowers that are blooming
	

We saw in Brute Force approach that traversing the whole list again for each person is not a good approach. So, to do it for efficiently, we can sort the start and end times of flowers in increasing order. Now, it is pretty obvious that, 

	If a flower started blooming at or before "time", then all flowers before it also started blooming at of before "time"
	If a flower stopped blooming before "time" then all flowers before it also stopped blooming before "time"
	
And that's the monotonicity we look for before going with Binary Search approach because it is important to know which way to move if "mid" is valid/not valid.

In both cases above, we can see that if "mid" is valid/not valid, all values before it are also valid/not valid. And so, if flower at "mid" has started blooming at or before time "t" then while on left side all flowers are valid, it is possible that on its right we have some more flowers that have started blooming at or before time "t". Hence, we will keep searching for the rightmost valid flower. 

Same with the other case where we want to find how many flowers have stopped blooming before "time".
