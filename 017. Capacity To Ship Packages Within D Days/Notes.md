# PROBLEM STATEMENT

A conveyor belt has packages that must be shipped from one port to another within days days.

The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

# EXAMPLE

    Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
    Output: 15
    Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
    1st day: 1, 2, 3, 4, 5
    2nd day: 6, 7
    3rd day: 8
    4th day: 9
    5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.


# HOW TO USE BINARY SEARCH TO SOLVE THIS PROBLEM?

It is not always necessary that we have to apply Binary search only on the input array. Sometimes, we apply binary search on some range that we think might have all the possible solutions for the problem. This is not given in the problem statement but we have to figure out this range and apply Binary Search on it. This method is called "**Binary Search On Answer**"

We will do the same in this problem. But how to think of this range? 

For that, just read the problem statement carefully. It asks us for the minimum weight capacity of the ship, such that all the packages can be shipped in given number of days. So, what we have to find is the minimum weight capacity. WE don't know that but we know the range of valid capacities right?

		E.g. If weights = [3,2,2,4,1,4]
		
		What can be the least weight capacity of the ship? 
		
		If you think, that would be 4. It cannot be any value less than 4.
		
		If it was 3, then we would not be able to load the package of weight 4 at all.
		
		So, the least weight capacity of a ship is the maximum weight in the array.
		
		
Now, if I ask you, what is the maximum possible capacity of a ship? 

It would be the sum of all the weights because that would mean we can ship all the packages in just one day.

So now, we got the range which is -

Maximum Weight in Array to the sum of all the weights

And this range includes all the values that can be the possible output. All the values in this range are valid for a specific scenario and because this range is always in the sorted order, that means we can apply Binary Search on it.


So if we get some mid value, then we have to then check if we can ship all the packages in given days if the minimum capacity for a day = mid.

And for that, I have a separate helper method which finds just that. If we cannot ship all packages in given days, this method returns False. 

And if it returns False, that means, all values before mid are also not going to be valid so no need to check those. So we need to search only on right side of mid.

But if we get True, that means mid is one possible solution. But since we want minimum capacity, we continue searching on left of mid.