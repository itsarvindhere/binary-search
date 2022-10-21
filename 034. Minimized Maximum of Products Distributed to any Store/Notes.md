# PROBLEM STATEMENT

You are given an integer n indicating there are n specialty retail stores. There are m product types of varying amounts, which are given as a 0-indexed integer array quantities, where quantities[i] represents the number of products of the ith product type.

You need to distribute all products to the retail stores following these rules:

    1. A store can only be given at most one product type but can be given any amount of it.
    2. After distribution, each store will have been given some number of products (possibly 0). Let x represent the maximum number of products given to any store. You want x to be as small as possible, i.e., you want to minimize the maximum number of products that are given to any store.

Return the minimum possible x.

# EXAMPLE

    Input: n = 6, quantities = [11,6]
    Output: 3

Explanation: One optimal way is:
- The 11 products of type 0 are distributed to the first four stores in these amounts: 2, 3, 3, 3
- The 6 products of type 1 are distributed to the other two stores in these amounts: 3, 3
The maximum number of products given to any store is max(2, 3, 3, 3, 3, 3) = 3.


# BINARY SEARCH ON ANSWER

This is yet another problem where we can use the concept of "Binary Search on Answer". It means, apply Binary Search on the range of possible valid solutions, not on input array.

	How can we identify Binary search in such problems? 

	For that, we have to figure out if there is monotonicity. 

	For example, we are asked to distribute all the products among "n" stores. 

	Now Consider this case -> we give each store at most "3" products and we are able to distribute all of them.

	So can I say that any value greater than "3" will also be valid? 

	Absolutely. 

	Because it makes sense that if we distribute at most "4" or "5" or any value more than "3" 

	then also we can distribute all of them, no matter if some stores get 0 products. 

	That's because "3" is valid so all values bigger than "3" will also be valid. 

	And so, it makes no sense to again check for bigger values than 3.

Does this sound familiar to Binary Search? Because it is! In Binary search too, we discard one half every time we check some condition at mid.

Now, Think about the range on which we will apply Binary search. As I said, the concept is called "Binary Search on Answer". Here, answer that we have to find is the minimum "x" value. What is "x" ? "x" is the maximum number of products a store can get.

	So, think about what can be the range of possible solutions or possible "x" values. 

	The maximum a store can get is the maximum value in "quantities" array. 

	Because it is also given in the problem that a store can also be given one product type.

	And the minimum can be 1 or 0. 

	Here, I took 1 as minimum to avoid any divide by zero exception.

So now, we have a range 1 to max(quantities) and this range will have the required minimum "x" value for any given input.

Every "mid" value we get is the "number of maximum products we can give to a store". And so, we just have to check if we can distribute all the products if a store does not get more than "mid" products. If yes, that means, no need to check for any value bigger than mid as all of them are also valid.

And since we are asked to minimize this value, we will keep searching for a smaller valid value on the left side of mid.

But if "mid" itself is not valid, no value less than "mid" can be valid. Hence, no use of searching on left side of mid in that case. And so, if mid is not valid, we need to search for a valid value on right side of mid.