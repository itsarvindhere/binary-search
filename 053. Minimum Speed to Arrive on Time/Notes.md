# PROBLEM STATEMENT

You are given a floating-point number hour, representing the amount of time you have to reach the office. To commute to the office, you must take n trains in sequential order. You are also given an integer array dist of length n, where dist[i] describes the distance (in kilometers) of the ith train ride.

Each train can only depart at an integer hour, so you may need to wait in between each train ride.

    For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can depart on the 2nd train ride at the 2 hour mark.

Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach the office on time, or -1 if it is impossible to be on time.

Tests are generated such that the answer will not exceed 107 and hour will have at most two digits after the decimal point.


# EXAMPLE

    Input: dist = [1,3,2], hour = 6
    Output: 1

Explanation: At speed 1:
- The first train ride takes 1/1 = 1 hour.
- Since we are already at an integer hour, we depart immediately at the 1 hour mark. The second train takes 3/1 = 3 hours.
- Since we are already at an integer hour, we depart immediately at the 4 hour mark. The third train takes 2/1 = 2 hours.
- You will arrive at exactly the 6 hour mark.

# BINARY SEARCH ON ANSWER - O(NLogN)

	This is one of those problems where we apply Binary Search on the Range of Answers, not on the given input.
	
	In other words - Binary Search on Answer.
	
	
In this approach, we first want a range of values that may be valid solutions. Here, we are asked for minimum speed. For a moment, forget the "minimum" part. What can be the range of speed? The smallest or minimum speed value can be 1. And since the problem says the answer cannot exceed 10^7, that can be the maximum speed value. And so, we get a range [1, 10^7] and our solution lies in this range only. And since this range is sorted, that means we can apply Binary Search.

Because what if a particular speed value is not valid? That simply would mean that any value less than that value is also not valid as that makes sense. Also, if a particular speed value is valid, that simply means, any speed higher is also valid. And in this problem, we are asked for minimize the valid speed.

So, at every "mid", we check if that "mid" value is a valid speed or not. If it is, it means, it is one possible solution. But since we want to minimize the speed, we continue our search on the left side of mid. But, if "mid" itself if not valid, then no value on its left can be valid too. So in that case, we will search on right side of mid.

Do note that when we calculate the time taken by each train, for the last train, we do not take the Integer time. That is why, for last train, we added the time taken outside the loop and we did not take the ceil value of this time. 