# PROBLEM STATEMENT

You are standing at position 0 on an infinite number line. There is a destination at position target.

You can make some number of moves numMoves so that:

   1. On each move, you can either go left or right.
   2. During the ith move (starting from i == 1 to i == numMoves), you take i steps in the chosen direction.

Given the integer target, return the minimum number of moves required (i.e., the minimum numMoves) to reach the destination.

# EXAMPLE

    Input: target = 2
    Output: 3

    Explanation:
    On the 1st move, we step from 0 to 1 (1 step).
    On the 2nd move, we step from 1 to -1 (2 steps).
    On the 3rd move, we step from -1 to 2 (3 steps).


# SOLUTION

This problem is all about observation and identifying the patterns.

	It is given that in one move, either we can go left or right. 
		
	Now first thing is that, no matter if the "target" is +ve or -ve, the number of moves will be the same. 

	For example, no matter if you have -3 or +3, both will take minimum 2 moves. 

	Hence, first thing we can do is to take the absolute value of the target 

	so we are not confused between +ve and -ve inputs.

Next, lets observe and try to find some patterns. Lets see at each move, where can we reach.

	Move 1 -> We reach 1
	Move 2 -> We reach 3
	Move 3 -> We reach 6
	Move 4 -> We reach 10
	
So first thing we can try doing is keep moving till We reach the target or just more than target. For example, if "target" is "10", then we will make 4 moves. And we can return the number of moves as we reached the target. But, suppose if target is "8". In that case, we will make 4 moves because we will reach 10 which is just more than 8 and we come out of our first loop.

Now, all that's left is to try to think how can we find the number of moves for numbers that cannot be reached directly by simply incrementing moves. e.g. for "8".

	When our first loop finishes, we would've taken 4 moves and our position will be 10, right?
	
	This means, we have moved to right of 8 by 2 extra steps.
	
	In other words, difference between our position and the target is 2. 
	
	So to mitigate that, what we can do is try to reverse a particular move 
	
	since at each move, we can move to left side as well.


If you try to see how many minimum moves we can take to reach 8, then that will be "4" moves. We have to reverse move "1" so that initialy we move from 0 to -1. Then we can take all other moves to right side only till we reach 8.

Now, since the difference between pos and target was 2, which was even, we could readjust one of our previous moves. But is this always the case for all types of inputs?

![image](https://assets.leetcode.com/users/images/c4a4e1dd-f430-47a4-862e-d0a7726246d5_1667720897.5475924.png)

What if target = "9". In that case, when we are at pos 10, then pos - target is 1. That is not an even number. This also means, there is no way we can reverse any one move right now to reach 9. You can try that, It will not work. We can never reach "9" with 4 moves.

And hence, the main idea is that, if our position becomes more than "target", then we need to ensure that the difference is an even number. If it is not, that means we need to add more moves till the difference is even.

So, when we are at pos = 10, and target = 9, we see that (pos - target) is not even. So, we increment moves to 5 and now our position becomes pos + 5 => 15.

Now we again check the difference. (15 - 9) => 6 and since 6 is an even number we stop. And we can now return the number of moves we have taken so far. That is, 5 moves. So, we can reach "9" in a minimum of 5 moves.

If you are wondering how this "even" difference concept is working, then that's because, when difference between "pos" and "target" is 2 or 4 or 6 or anything even, then that means, we have to reduce our position by "2" or "4" or "6" to reach target. 

	We saw that in case of target = 8, initially, we got position as 1 + 2 + 3 + 4 = 10

	If you take any move and reverse it, you will see that the overall position value will be reduced by (2 * move).

	For example, if we go to left side in move 1, then our position is like ->
		
	-1 + 2 + 3 + 4 => 8

	And this (2 * move) is the reason why we want the difference to be an even number. 
	
	Because if we reverse any move, it will always reduce the position by an even difference.

Take another example of "target" = 9.

When pos = 10, then difference is 1. There is no way we can reverse any move such that position is reduced by 1. Position can reduce by either 2, 4, 6, 8, 10 and so on depending on what move we reverse.

So we have to keep moving until difference is even. Hence, we reach pos = 15. Now our difference between pos and target is 6 (15 - 9).

This means, now we can reverse move 3 such that it results in (2 * 3) difference in the position and we reach 9.
	
![image](https://assets.leetcode.com/users/images/02c7a757-8bed-430c-922e-fb63f6c667f3_1667721783.7530348.png)