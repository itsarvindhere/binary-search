# PROBLEM STATEMENT
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt

# BINARY SEARCH APPROACH

We know the square of a number is in range 1 to N/2

So, if in this range, some number, X, is not squaring up to num, then why bother checking any number less than X?

Similarly, if some number, X, has square more than num, why bother checking any number greater than X?

That's the whole point in this Binary Search approach.