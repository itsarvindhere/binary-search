# PROBLEM STATEMENT

You have n computers. You are given the integer n and a 0-indexed integer array batteries where the ith battery can run a computer for batteries[i] minutes. You are interested in running all n computers simultaneously using the given batteries.

Initially, you can insert at most one battery into each computer. After that and at any integer time moment, you can remove a battery from a computer and insert another battery any number of times. The inserted battery can be a totally new battery or a battery from another computer. You may assume that the removing and inserting processes take no time.

Note that the batteries cannot be recharged.

Return the maximum number of minutes you can run all the n computers simultaneously.

 
# EXAMPLE
    Input: n = 2, batteries = [3,3,3]
    Output: 4

Explanation: 
Initially, insert battery 0 into the first computer and battery 1 into the second computer.
After two minutes, remove battery 1 from the second computer and insert battery 2 instead. Note that battery 1 can still run for one minute.
At the end of the third minute, battery 0 is drained, and you need to remove it from the first computer and insert battery 1 instead.
By the end of the fourth minute, battery 1 is also drained, and the first computer is no longer running.
We can run the two computers simultaneously for at most 4 minutes, so we return 4.

# BINARY SEARCH ON ANSWER APPROACH

This is a problem where we have to "Maximize" some value. Here, we are asked to Maximize the Running Time of "n" computers. How can we use Binary Search in this case? For that, we have to first figure out the monotonicity.

If we can run "n" computers simultaneously for "x" minutes, then it makes sense that we can also run them simultaneously for any value than is less than "x", right?

Similarly, if we cannot run "n" computers simultaneously for "x" minutes, then it makes sense that no value greater than "x" can be valid. 

And that's the monotonicity we are looking for. In this case, we can use Binary Search. More specifically, we have to apply Binary Search on the range of values that we think can be the possible "Running time" values. 

The lower bound of this range can be 0 or 1. That is, suppose there is only one computer and only one battery with 1 minute of charge. In that case, we can run this computer for 1 minute only.

Similarly, what can be the maximum running time? That's what we have to find. But we can take the sum to be the upper bound. 

Even better is to take  (sum of all the minutes / n) as the upper bound (Thanks to the Leetcode's Discuss Tab)

And now, we have this range [1, sum(batteries)/n] in which we know the answer will be found. On this range, we will apply Binary Search and for each "mid" value, we have to consider this value as the "Running Time". So, we have to then find if we can run "n" computers for "mid" minutes simultaneously. For that, we have a separate helper method "isValid".

This is the most tricky part in this problem - To Write the helper method which checks if we can run "n" computers simultaneouly for "x" minutes.

To understand how we can check, let's take an example.

	batteries = [2,3,2,1,7,8,2,4]
	n = 4
	x = 5
	
	So, we want to check if we can run 4 computers simultaneously for 5 minutes.
	
	Now, think about how can we use the batteries. 
	
	___________________________________________________________________
	
	Let's first take the bigger batteries. Since we want computer1 to run for "5" minutes
	We simply attach the battery[5] with "8" minutes of charge to it. 
	Do note that we only need "5" minutes from this battery. 
	
	___________________________________________________________________
	
	For computer2, we do the same. We attach it to the battery[4] with "7" minutes of charge
	
	___________________________________________________________________
	
	Now, we are at computer3. We need "5" minutes so for this one, we can use 
	batteries[0] and batteries[1] which in total give us 2 + 3 => 5 minutes
	
	___________________________________________________________________
	
	Finally, we have computer4. For this one, we can use batteries[2], batteries[3] and batteries[6]
	giving us 2 + 1 + 2 => 5 minutes
	
	So, yes, we can run 4 computers simultaenously for "5" minutes. 
	
	But is it the maximum running time? That's what we have to find.
	
	
Did you notice something? If the battery has less than "x" minutes, then we will use it fully. On the other hand, if a battery has >= x minutes of charge, then we will only use at most "x" minutes out of it. We saw this in case of computer1 where we had "8" minutes of charge but we needed only "5" minutes so we only took 5 minutes. And that's the whole idea of the helper method.

We want to find what will be the total running time if we have to run a computer for "x" minutes. We will keep adding the minutes to this runningTime, depending on whether battery has less than "x" minutes of charge or >= x minutes of charge.

And once we get the runningTime, since we have the running time for one computer as "x", we can easily find how many computer can we run by doing "runningTime / x". We want this value to be at least "n". That is, we should be able to run at least "n" computers.