# PROBLEM STATEMENT

You are given an integer array bloomDay, an integer m and an integer k.

You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.

The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.

Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.

# BINARY SEARCH ON ANSWER

This is one of those problems where we have to make use of the "Binary Search on Answer" concept.

	In simple words - Apply Binary Search on the range of possible solution values.
	
Here, we have to find "minimum days to wait" to make m bouquets.

Now, What can be the range of values in which solution can exist?

We have to think of what can be the smallest possible input? We might be asked for 1 bouquet that can be make using 1 flower only.

So in that case, what is the minimum days we need to wait?
		
		Consider this example - 
		
		bloomDay = [1,10,3,10,2], m = 1, k = 1
		
		We can see that bloomDay[0] has value = 1 which means this flower will bloom after waiting for 1 day only.
		
		And since we only need 1 flower, the minimum days we need to wait is 1. Because 1 is the smallest value in this array.
		
		And this is the lower bound of our range.
		
		
Similarly, think of what can be the upper bound?

What if we are asked to make one bouquet but that will be made using all the flowers that we have in array. 

		Consider this example - 
		
		bloomDay = [1,10,3,10,2], m = 1, k = 5
		
		So, to get all the 5 flowers ready for bouquet, we have to wait 10 days, right? 
		
		Because only then the flowers at index 1 and index 3 will bloom. 
		
This means, the upper bound of the range is the maximum value in the given array.

Hence the Range is - 

		Minimum Value in bloomDay 
						To
		Maximim Value in bloomDay
		
And we are sure that solution for any test case lies in this range only.

And since this range is sorted, we can use Binary search to get the minimum valid value.

	bloomDay = [1,10,3,10,2], m = 3, k = 1
	
	Here, range is from 1 to 10
	
	So, we get mid = 5
	
	Now, how to check if we can wait 5 days to make m bouquets?
	
	That's where we can use a Helper method that checks just that.
	

We will go through the array and for every flower, we check if it can bloom in <= mid days. IF yes, we can take this flower. But it is also important to note that we need adjacent flowers. So, if some flower takes longer days to bloom, then that means, we have to again start searching for k adjacent flowers from 0.

If we got k adjacent flowers, we can make one bouquet

And when loop ends, we just need to check whether we were able to make at least "m" bouquets after waiting for "mid" days.