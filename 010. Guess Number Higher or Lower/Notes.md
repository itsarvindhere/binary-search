# PROBLEM STATEMENT
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

    -1: Your guess is higher than the number I picked (i.e. num > pick).
    1: Your guess is lower than the number I picked (i.e. num < pick).
    0: your guess is equal to the number I picked (i.e. num == pick).
    Return the number that I picked.


## **WHY IS THIS A BINARY SEARCH PROBLEM?**

        1. First of all we have range from 1 to n so it is in sorted order
        2. Second, if some value is lower than guessed number, all values lower than that are also not valid
        3. Similarly, if some value is higher than guessed number, all the values higher than that are also not valid