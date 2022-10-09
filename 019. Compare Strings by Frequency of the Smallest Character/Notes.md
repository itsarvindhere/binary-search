# PROBLEM STATEMENT

Let the function f(s) be the frequency of the lexicographically smallest character in a non-empty string s. For example, if s = "dcce" then f(s) = 2 because the lexicographically smallest character is 'c', which has a frequency of 2.

You are given an array of strings words and another array of query strings queries. For each query queries[i], count the number of words in words such that f(queries[i]) < f(W) for each W in words.

Return an integer array answer, where each answer[i] is the answer to the ith query.

# EXAMPLE

    Input: queries = ["cbd"], words = ["zaaaz"]
    Output: [1]

Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").


# WITHOUT SORTING OR BINARY SEARCH

Yes, we can solve this problem without Sorting or Binary search. That's because just look at the constraints that we are given. 

			1 <= queries[i].length, words[i].length <= 10
			
This means, the string in any of the two arrays can be of maximum 10 length. What that means is that the frequency of smallest character can be at least 1 or at most 10. Not more than that. 

It will be 1 if there is either only one character or only one smallest character. 
It will be 10 only if there are 10 same characters.


So, we can store the count of frequency of smallest character for words array.

	e.g. words = ["a","aa","aaa","aaaa"]

	So, we can see that "a" has freq of smallest as 1
	Similarly, for "aa", it is 2
	For "aaa" it is 3
	for "aaaa" it is 4

So, we can keep track of how many strings have frequency 1, how many have 2 and so on till 10. And for any test case, we will use the same 10-sized frequency array. 


	So, for words = ["a","aa","aaa","aaaa"], our frequency array becomes - 
	
	freqArr = [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
	
	Each index = frequency of smallest character
	
	So, value at index = 1 means what is the count of strings in which frequency of smallest character is 1
	
	
Now, once we get this array, what to do next? 

We know that for each query, we have to count all those words for which freq of smallest is larger.

So we can easily find that by first finding the frequency of smallest for the query string, and then, we need to see how words are there for which frequency of smallest character is more than that of query string.

	e.g. queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
	
	freqArr is [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
	
	Now we start with "bbb". We see that for it, freq of smallest is 3
	
	So, we need to count all those words for which freq of smallest is > 3
	
	That is, sum of all values in freqArr from index = 4 to index = 10
	
	And instead of finding the sum in each iteration, why not use prefix sum for this?
	
	prefixSum of freqArr is [0, 1, 2, 3, 4, 4, 4, 4, 4, 4, 4]
	
	So, the last value is the total sum.
	
	And value at each index shows how many words have frequencies <= index
	
	e.g. at index = 2, we have 2. This means, there are 2 words with freq of smallest word <= 2
	
	And indeed we have two words -> "a" and "aa".
	
	So now, since for "bbb" we have freq of smallest = 3
	
	We want the count of words with freq of smallest > 3
	
	And that is pretty straightforward.
	
	Count of words with freq of smallest character > 3 =   Words with freq of smallest <= 10 - Words with freq of smallest <= 3
	
	So for "bbb", it will be 4 - 3 => 1
	
	And for "cc" it will be 4 - 2 => 2
	
	
	Hence output array will be [1,2]