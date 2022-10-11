# PROBLEM STATEMENT

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.


# EXAMPLE

    Input: nums = [1,1,2,3,3,4,4,8,8]
    Output: 2

# BINARY SEARCH APPROACH - O(LogN)

This problem asks us to write an O(LogN) solution which just means solve using Binary Search.

To write Binary Search solution, we need to make some observations.

Lets see how an array would look like if there was no single element.

		 nums = [1,1,2,2,3,3,4,4,8,8]
		 
		 So, if there was no single element, we see that, 
		 
		for every element, first occurance is at even index
		And second occurance is at odd index
		
Now lets factor in the single element.
		
		nums = [1,1,2,3,3,4,4,8,8]
		
		Did you notice what happened?
		
		Here, 2 is the single element.
		
		Instantly, this single element disturbed the right side such that,
		
		For every element on right side of single element - 
			first occurance is now at odd index
			second occurance is at even index
			

This means, we can use this property of occurances to figure out whether the single element is on left side of any index or right side of any index. Beacuse that is the most important thing to find out in a Binary search approach i.e., to move to left of mid or right of mid.

		
		nums = [1,1,2,3,3,4,4,8,8]
			
		Initially, start = 0, end = n - 1
		
		We get mid index as -> 4
		
		Now, 4 is an even index, right? So - 
		
			If its duplicate is on its left side or at odd index,
			then it means, some single element disturbed this order
			In other words, this would mean that single element is on left side of mid
			
			If duplicate was on its right, then this would've meant that single element is not on left. 
			So in that case, we would've searched on the right side.
			
		If the mid index was odd index, then also we would do a similar check
		
			If the duplicate of mid is on its right side, i.e., at even index,
			then also it means that some single element disturbed this order
			And so, the single element is on left side of mid
			
			
In simple words -> 

		If the indices of duplicate elements are in order -> "odd , even", that means the single element is on the left
		If the indices of duplicate elements are in order -> "even, odd" then single element is on the right side