# PROBLEM STATMENT

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

# EXAMPLE

    Input: piles = [3,6,7,11], h = 8
    Output: 4

# BINARY SEARCH ON ANSWER

We are asked for the minimum per-hour eating speed. So, what we can think of is the range of valid solutions.

For that, the simplest way is to think of scenarios. 

Forget about "minimum" for now. Lets say we were asked for simply the eating speed.

Then, what can be the possible valid values? Ofcourse those values will be in the range of slowest eating speed to fastest eating speed

	e.g. What can be the slowest possible eating speed?
	
	We know that there is at least 1 banana in each pile
	
	Which means, the slowest eating speed can be 1 banana per hour
	
	In that case, 
		Koko will take same amount of hours to eat all bananas off a pile as the number of bananas in that pile
		
	And this will be the lower bound of our Range of valid solutions.
	
	Now, think of what can be the fastest possible eating speed?
	
	It is given that Koko can eat from only one pile in an hour. 
	
	This means, we cannot simply say - Why not eat all the bananas from all piles in one hour.
	
	Since she can eat from one pile in an hour, the fastest speed will be the one that ensures each pile is finished in an hour
	
	And that will be possible if Koko can eat same number of bananas in an hour as the maximum bananas in any pile
	
	If that sound confusing, take this example - [1,2,3,10] and h = 5
	
	If Koko can finish all piles in len(piles) hours then that will the fastest eating speed.
	And she can ensure that if the eating speed is 10 i.e., maximum value in the array
	
	Because now we can see that if she can eat 10 bananas in an hour, then she can finish each pile in 1 hour.

	And that's the upper bound of our range.
	
Hence, we will apply Binary search on this range 1 to max(piles)