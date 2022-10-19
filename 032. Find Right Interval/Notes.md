# PROBLEM STATEMENT

You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.

The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. Note that i may equal j.

Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i.

# EXAMPLE

    Input: intervals = [[3,4],[2,3],[1,2]]
    Output: [-1,0,1]

Explanation: There is no right interval for [3,4].
The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.

# BRUTE FORCE APPROACH - O(N^2)

The Brute Force Approach is quite straightforward.

For every interval i, try to find an interval j, where start value of j is >= end value of i interval. Since we are asked to minimize the "start" value of j, we have to keep sarching till the end because we want the interval j with smallest "start" value that satisfies the condition.

If we don't get any such interval, we just append -1 in the result list,

But this approach won't work for large lists and hence will show TLE for some test cases.

But using this approach, we can try to write an optimized solution.


# BINARY SEARCH APPROACH - O(NLogN)

What if we sort the given Intervals list? Since each interval is having [start, end], when we sort it, list will be sorted based on the start value. So now, instead of a linear search, we can use Binary Search to reduce the time complexity from O(N^2) to O(NLogN).


Now, for each interval "i", we have to binary search for an interval "j" such that the start value of j >= end value of i. And since the list is sorted based on start values, if we get any such start value which satisfies this condition, we know that all the start values after it are also valid. But, we are asked for a minimum start value. Which means, even if we find any interval j that satisfies the condition, we keep searching for an interval with an even smaller start value which also satisfies the condition. Hence, we keep searching on left side of mid in this case.

One important thing to note is that, in the result array, we have to output the index of "j" interval for every "i" interval. And these indices need to be the same as in the original list, not what we have after sorting. So, we also need to store the original indices of start values before sorting the list. The biggest hint is given in the problem itself which says -> 
			
						each start value is unique
						
So we can simply use a map and keep the indices of each start value in it. So that as soon as we find an interval "j" that satisfies the condition, we can get the original index of it from the map. And put that in the result array.

