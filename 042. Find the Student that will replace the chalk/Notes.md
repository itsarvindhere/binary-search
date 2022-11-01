# PROBLEM STATEMENT

There are n students in a class numbered from 0 to n - 1. The teacher will give each student a problem starting with the student number 0, then the student number 1, and so on until the teacher reaches the student number n - 1. After that, the teacher will restart the process, starting with the student number 0 again.

You are given a 0-indexed integer array chalk and an integer k. There are initially k pieces of chalk. When the student number i is given a problem to solve, they will use chalk[i] pieces of chalk to solve that problem. However, if the current number of chalk pieces is strictly less than chalk[i], then the student number i will be asked to replace the chalk.

Return the index of the student that will replace the chalk.

# EXAMPLE

    Input: chalk = [5,1,5], k = 22
    Output: 0
    Explanation: The students go in turns as follows:
    - Student number 0 uses 5 chalk, so k = 17.
    - Student number 1 uses 1 chalk, so k = 16.
    - Student number 2 uses 5 chalk, so k = 11.
    - Student number 0 uses 5 chalk, so k = 6.
    - Student number 1 uses 1 chalk, so k = 5.
    - Student number 2 uses 5 chalk, so k = 0.
    - 
Student number 0 does not have enough chalk, so they will have to replace it.


# BRUTE FORCE APPROACH

In Brute Force approach we keep iterating the array again and again until k becomes less than any chalk[i]. Ofcourse this will not work for inputs where k is huge and values in array are very small compared to k.

	e.g. what if we have chalk = [1,2,3] and k = 100000000
	
So, we will be iterating the array again and again and again and it will take forever to make k less than any of the three values.

# OPTIMIZED APPROACH

Did you notice the reason why above approach failed? It is because when k is more than the sum of the whole array, we have to again start iterating the array from beginning. 

Just think what we are doing in each iteration. We are reducing k by each element. Or in other words, we are reducing k by the sum of the array.

If x is the sum of the array, then this is what happens - 

		First iteration -> k = k - x
		Second iteration -> k = k - x
		Third iteration -> k = k - x
		
So we keep doing it until k becomes less than any value in array.

To avoid this, what we can do is mod "k" by the sum of the array. This will reduce the value of "k" such that we can then find the required index in just one iteration. So we don't have to go round and round and round.

# BINARY SEARCH + PREFIX SUM APPROACH

Since this problem is tagged under Binary Search, we can also try to do it using Binary Search. In above approach we saw that after we do k mod sum, we can then find the required index in just O(N) time. 

In this O(N) loop, what we are doing is - 

		First iteration -> k = k - chalk[0]
		Second iteration -> k = k - chalk[1]
		Third iteration -> k = k - chalk[2]
		
		So, basically we are doing ->  k - (chalk][0] + chalk[1] + chalk[2])
		
		Untill k becomes less than any value.
		
		
To use Binary Search, we have to first convert the array in a prefix sum array. Why?

	Take this example -> [3,1,2,4], k = 25
	
	Since sum of array is 10, after we do k mod sum, we get k = 5
	
	In each iteration, we will reduce k by chalk[i] value.
	
	It means, when we reach the index at which k is < chalk[i], 
	
	we would've reduced the value of k by the sum of values from 0 to ith index (excluding i)
	
	Now you are getting the idea of prefix sum, right?
	
	When we convert the above array in a prefix sum array, we get - 
	
	[3,4,6,10]
	
	As mentioned above, we are doing  k - (chalk][0] + chalk[1] + chalk[2])
	
	And we stop when k - (chalk][0] + chalk[1] + chalk[2]) becomes less than zero
	
	That is, when chalk[0] + chalk[1] + chalk[2] becomes greater than k
	
	And that's what each value in prefix sum array shows. 
	
	For example, 
	
		at 0th index, prefix sum array has 3. It means, that's the value of chalk[0]
		at 1st index, prefix sum array has 4. It means, that's the value of chalk[0] + chalk[1]
		at 2nd index, prefix sum array has 6. It means, that's the value of chalk[0] + chalk[1] + chalk[2]
		
	We see that when k = 5, then when we reach the index = 2, then  chalk[0] + chalk[1] + chalk[2] becomes 
	greater than k. And that's the index that we need to return.
	
So using Binary Search, all we need to find is the first index at which value is > k