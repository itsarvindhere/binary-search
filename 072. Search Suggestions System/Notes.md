# PROBLEM STATEMENT

You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.

# EXAMPLE

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"

Output: [["mobile","moneypot","monitor"],["mobile","moneypot","monitor"],["mouse","mousepad"],["mouse","mousepad"],["mouse","mousepad"]]

Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"].
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"].
After typing mou, mous and mouse the system suggests ["mouse","mousepad"].


# APPROACH

Since we want the result in the lexicographical order, it makes sense to think that sorting will be used in the solution.

Just think this way.  If the list of products is already in the sorted order, then as we find matching words, then we can put them in the matching list without having to think of the order again because the list is already sorted. 

In short, we only have to sort the list once and then, the only thing left is to find matching words. We don't have to care about the lexicographical order of the matching words that we will find because we know the list is sorted.

## **1. BRUTE FORCE SOLUTION**

In the Brute Force approach, for each prefix (prefix of searched word), we will scan the whole list of products and see what all words have matching prefix. All of those will be matching words.

For example, Suppose we have 

	products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
	
	Sorted list -> ["mobile","moneypot","monitor","mouse","mousepad"]
	
	When we search "m", then all the words are matching
	Because all of them have same prefix "m"
	
	When we search "mo" then also all words will match
	
	But when we search "mou" then only the last two words will match ["mouse", "mousepad"]
	
But, the issue with this approach is that, since for each prefix, we are linearly scanning the products list, the time complexity turns out as O(N^2).

## **2. BINARY SEARCH SOLUTION**

Since the list is already sorted, we can avoid linear scan and instead, use Binary Search on the products list. To understand that, let's take the same example again. I added another word  "movie" in there just to make it easy to understand the logic of Binary Search. 

	products = [ "movie", "mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
	
	Sorted list -> ["mobile","moneypot","monitor","mouse","mousepad", "movie"]
	
	When we searched "mou", then we saw that no word before "mouse" was valid
	And similarly, no word after "mousepad" was valid.
	
	So, if we somehow get these two indices before and after which no matching words are present,
	Then we can easily say that all words between these two indices are the matching words.
	
	Makes sense, right?
	
And to find these two indices, we will use Binary Search.

So basically, we are looking for the leftmost index in the products list which has a word with same prefix.
And the rightmost index in the products list which has the word with the same prefix.

	Sorted list -> ["mobile","moneypot","monitor","mouse","mousepad", "movie"]
	
	Suppose, searched prefix is "mou"
	
	When we apply binary search, start = 0, end = 5
	
	mid will be 2 and at index "2" we have word "monitor"
	
	Now, we see that the prefix does not match "mou"
	
	But, how do we decide whether to go to left side of right side of mid?
	
	Here, we can see that prefix for  "monitor" is "mon"
	And "mon" is lexicographically smaller than "mou"
	
	What does this mean?
	
	It means that not only "monitor",
	but no word before "monitor" will have a matching prefix since the list is sorted.
	
	And so, in this case, we search on right side of mid.
	
	But, if it was other way around, that is, the prefix at mid was greater than "mou"
	Then, we would've searched on left side of mid 
	because we would've never found a matching word on right side of mid
	
And so, putting all this together, we have the Binary Search solution for this problem.