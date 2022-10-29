# PROBLEM STATEMENT

There is a long table with a line of plates and candles arranged on top of it. You are given a 0-indexed string s consisting of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.

You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the substring s[lefti...righti] (inclusive). For each query, you need to find the number of plates between candles that are in the substring. A plate is considered between candles if there is at least one candle to its left and at least one candle to its right in the substring.

    For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". The number of plates between candles in this substring is 2, as each of the two plates has at least one candle in the substring to its left and right.

Return an integer array answer where answer[i] is the answer to the ith query.

# EXAMPLE

    Input: s = "**|**|***|", queries = [[2,5],[5,9]]
    Output: [2,3]

    Explanation:
    - queries[0] has two plates between candles.
    - queries[1] has three plates between candles.


# BINARY SEARCH APPROACH

It is given that for each query, we need to find how many plates are there between candles. The important thing to note is "BETWEEN CANDLES". It means, all the valid plates for any substring will have at least one candle on the left and on the right side.

And so, for a substring, we try to find the leftmost candle and the rightmost candle.

If we can find that, all that's left now is to count how many plates are between these candles. And to avoid doing that calculation separately for each query, we can have a prefix sum array in which we precompute at every index, what is the number of plates so far.

To find the leftmost candle index and rightmost candle index, we can use Binary Search.