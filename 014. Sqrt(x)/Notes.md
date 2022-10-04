# PROBLEM STATEMENT
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.


# BRUTE FORCE - O(√N)

Not exactly Brute force, but a better version of Brute Force that does not give TLE.

Basically, we start from 1 and keep checking the square of that number to see if it gives us x or not. If it does, great! Just return that number.

If it does not, then either the square is less than x or more than x. If less than x, we continue with next numbers. Otherwise, if square is more than x, that means the given number is not a perfect square to we will return the previous number.

# BINARY SEARCH - O(LogN)

Why are we bothering to check each number?

Since the range 2 to x is sorted already, just apply Binary Search. We need to search a number that squares up to x.

If the square is less than x, search on right of mid, otherwise on left of mid.

For x values that are not perfecrt squares, just return the "end" value after Binary Search ends.