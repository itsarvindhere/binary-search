# PROBLEM STATEMENT

You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.

Return this maximum sum.

Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.

# EXAMPLE

    Input: events = [[1,3,2],[4,5,2],[2,4,3]]
    Output: 4

# BRUTE FORCE APPROACH - O(N^2)

In Brute Force approach, we just do what the problem asks us to do. We don't care about how efficient this solution is. But if you are able to write a Brute Force Approach, you can think of an Optimized Solution easily.

Since we are asked to find two non overlapping events, we can check for that by making sure that the second event starts after the first has finished. Since it is possible that for any ith event, an event with start time greater than end time of ith event can be before it in the list, we have to traverse the whole array from beginning for every event to find a valid event to pair.

Hence, this approach has an O(N^2) complexity. It will not work for large inputs and we will get TLE.

# BINARY SEARCH APPROACH - O(NLogN)

We know that if an algorithm has O(N^2) time complexity and it is not working for large inputs, a better approach is to try to make it at least O(NLogN). 

Converting that N to LogN complexity means instead of Linear Search in the second for loop, we need to use Binary Search. But to use Binary Search, our array needs to be sorted. 
 
Notice that in Brute Force, one issue is that for each event, we have to traverse the list from the beginning to find an event whose start time is greater than the end time of ith event.

	Now, just think about it - What if our events list is already sorted based on start time?

	In that case, if we can find an event that is valid, then all the events after it are also valid because array is sorted. 
	
	Consider this example ->
	
			events = [[1,3,2],[4,7,3],[5,8,5], [6,4,10]]
			
			If we take the first event => [1,3,2]
			
			For it, start time = 1 and end time = 3
			
			It means, any event that has start time > 3 can be paired with this event.
			
			And we see that [4,7,3] is a valid event since its start time is 4 and 4 > 3
			
			But since our list is already sorted based on start times, 
			it also means, all events after [4,7,3] are also valid and can be paired with [1,3,2]
			
			Now you got the idea, right?
			
			
	So, all that we need to find is this leftmost event that is valid 
	because we know all events after it will be valid as well.

Once we can find such an index, then all that is left to find is what is the maximum possible value in [leftmostindex, end of list] subarray.

But if we try to find that for each event, that again results in an O(N^2) complexity because to find that max value in a certain interval, we again have to do linear scan as values are not sorted.

Hence, the only option is to find a way to precompute this maximum possible value on the right side of each index such that we can find the maximum value in any range [leftmostindex, end of list] in O(1) time.

Therefore, before we even start with Binary Search, we have to precompute the maximum value on the right side for each event.