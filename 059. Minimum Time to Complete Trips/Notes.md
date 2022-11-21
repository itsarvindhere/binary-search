# PROBLEM STATEMENT

You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.

Each bus can make multiple trips successively; that is, the next trip can start immediately after completing the current trip. Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.

You are also given an integer totalTrips, which denotes the number of trips all buses should make in total. Return the minimum time required for all buses to complete at least totalTrips trips.

# EXAMPLE

    Input: time = [1,2,3], totalTrips = 5
    Output: 3

Explanation:
    - At time t = 1, the number of trips completed by each bus are [1,0,0]. 
    The total number of trips completed is 1 + 0 + 0 = 1.
    - At time t = 2, the number of trips completed by each bus are [2,1,0]. 
    The total number of trips completed is 2 + 1 + 0 = 3.
    - At time t = 3, the number of trips completed by each bus are [3,1,1]. 
    The total number of trips completed is 3 + 1 + 1 = 5.

So the minimum time needed for all buses to complete at least 5 trips is 3.

# BINARY SEARCH ON ANSWER APPROACH

This is yet another problem where we can use "**Binary Search on Answer**" approach to solve it.

In this approach, we first define the range of possible valid values for whatever we are asked for. Since here, we are asked for the "Minimum Time to Complete at least 'totalTrips'", what can be the lower and upper bound?

That is, what is the smallest possible value? 
	
	For that, consider this test case -> time = [2] and totalTrips = 1

	It means, there is only one bus and we have to complete at least 1 trip. 

	But since this bus takes "2" units of time to complete 1 trip, 

	it means, the minimum time to complete at least 1 trip is "2".
	
	That is, the lower bound is the minimum value in the "time" array
	
	Because we have to take at least that amount of time to complete at least 1 trip
	
Now, think of what can be the upper bound. For upper bound, simply consider a case with the maximum possible value for time[i] and totalTrips. Since both can be upto 10^7, take a test case -> time - [10000000] and totalTrips = 10000000

Here, again, there is only 1 bus. And this time, for 1 trip, this bus takes "10000000" unit of time. This means, to complete at least "10000000" trips, the time taken would be "10000000 * 10000000" or "10^14". And so, that would be the upper bound.

And now, in this range, we can apply Binary Search. Why? Because there is monotonicity. 

	If we can complete at least "totalTrips" in "x" time, 
	then ofcourse we can also complete them in any time more than "x"
	
	Similarly,
	
	If we cannot complete at least "totalTrips" in "x" time,
	then we cannot complete them in any time less than "x"

When we apply Binary Search on this range, at each "mid", we check whether in this "mid" time, all buses can complete at least "totalTrips" trips. For that, we have a helper method "isValid". If a bus takes "t" time to complete 1 trip, then in "mid" time, it will complete "mid/t" trips. And that's the idea to calculate how many trips each bus will complete in "mid" time. And when we sum all of those, if the number of trips are at least "totalTrips" then "mid" is one valid solution. 

And since we are asked for the "Minimum" value, we will store this "mid" value and then continue searching on left side of mid.

If "mid" itself is not valid, it make no sense to search on left side of mid since all values to left will be smaller than mid and hence won't be valid if "mid" itself is not valid. So, in that case, we search on the right side of mid.