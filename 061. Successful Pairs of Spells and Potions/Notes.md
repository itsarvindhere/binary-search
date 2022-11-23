# PROBLEM STATEMENT

You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

# EXAMPLE

    Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
    Output: [4,0,3]

Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
- 
Thus, [4,0,3] is returned.

# BRUTE FORCE APPROACH - O(N * M)

First, we will try to write a Brute Force solution. Yes, it will not work and will give TLE since the length of the input lists can be up to 10^5. But, this Brute Force approach will help us in figuring out the optimized solution.

We are asked to find how many potions are there for each spell such that spell * potion is >= success. So, we simply have two nested loops and for each spell, we loop through each potion and check if the condition is satisfied or not. If yes, we have a pair so we can increment the count. And finally, we set the count for that spell in the output list.

# SORTING + BINARY SEARCH APPROACH - O(MLogM + NLogM)

The reason why above solution gave TLE for large inputs is because for each spell, we have to loop through the entire potions list. But what if the potions list was sorted in increasing order? Then, if one potion can make a pair with a spell, then ofcourse all the potions after it can do that since the list is in an increasing order.

And that's the idea of this approach. We first sort the potions list in increasing order and then, for each spell, we Binary search for the leftmost index in the potions list where we have a valid potion to make a pair. And once we find that, then we know that all potions after it are also valid so total number of valid potions for that spell are simply -> (length of potions list - leftmost valid index)