# PROBLEM STATEMENT

You are given a 2D integer array items where items[i] = [pricei, beautyi] denotes the price and beauty of an item respectively.

You are also given a 0-indexed integer array queries. For each queries[j], you want to determine the maximum beauty of an item whose price is less than or equal to queries[j]. If no such item exists, then the answer to this query is 0.

Return an array answer of the same length as queries where answer[j] is the answer to the jth query.

# EXAMPLE

    Input: 
        items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
        queries = [1,2,3,4,5,6]
    Output: 
        [2,4,5,5,6,6]

Explanation:
- For queries[0]=1, [1,2] is the only item which has price <= 1. Hence, the answer for this query is 2.
- For queries[1]=2, the items which can be considered are [1,2] and [2,4]. 
  The maximum beauty among them is 4.
- For queries[2]=3 and queries[3]=4, the items which can be considered are [1,2], [3,2], [2,4], and [3,5].
  The maximum beauty among them is 5.
- For queries[4]=5 and queries[5]=6, all items can be considered.
  Hence, the answer for them is the maximum beauty of all items, i.e., 6.

# BRUTE FORCE APPROACH

The pretty straightforward way is to use two nested loops. For each query, go through each item and get the maximum beauty for an item whose price <= query. Will give TLE for large inputs.

# USING SORTING AND REDUCING ITERATIONS

Did you notice what we are doing again and again? What if the new query is greater than previous one? Is there any need to again start the inner loop from beginning? NO! because we can pick from where we left last time as we know that till that index, we have already found the maxBeauty. And that's the idea of this approach.

# BINARY SEARCH

It is not possible to apply the Binary Search directly to the items because they are sorted based on the price whereas we have to find the maximum beauty value. So it is possible that an item with less price has a higher beauty value than an item with a higher price.

Hence, before applying Binary search, we want to get rid of this issue with max beauty. What if we precompute the max beauty value till each index? If we can do that, all that's left is to apply Binary Search on items list to find the highest price that is <= query.