# PROBLEM STATEMENT

You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where:

    difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
    worker[j] is the ability of jth worker (i.e., the jth worker can only complete a job with difficulty at most worker[j]).

Every worker can be assigned at most one job, but one job can be completed multiple times.

    For example, if three workers attempt the same job that pays $1, then the total profit will be $3. If a worker cannot complete any job, their profit is $0.

Return the maximum profit we can achieve after assigning the workers to the jobs.


# EXAMPLE

    Input: 
        difficulty = [2,4,6,8,10]
        profit = [10,20,30,40,50]
        worker = [4,5,6,7]

    Output: 100
    
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.


# BRUTE FORCE - O(N^2)

In the Brute Force approach, for every worker, we go through every difficulty and if the worker can do that job, we check if it can give him a profit greater than previous job. If yes, update the maximum profit for that worker.

In the end, we add this maximum profit to the final output that we have to return.

The issue is that the arrays can be of up to 10^4 length. So, an O(N^2) solution will fail for large inputs and will show TLE.

But from this solution, we can start thinking about the Optimized Approach.

# BINARY SEARCH - O(NLogN)

The reason of O(N^2) complexity in Brute Force approach is that inner loop. For every worker, we have to iterate from the beginning to the end to find the maximum profit. 

	But what if the difficulties were in sorted order already?

In that case, if a worker is able to do any job with difficulty[i], then we can say that he can also do any job that has a lower difficulty right? In other words, in that case, we don't worry about the difficulties on left side as they will all be valid as the array is sorted. And that's the idea of Binary Search. 

So using Binary Search, all we have to do is find the rightmost valid difficulty out of the sorted difficulty list. Once we can find that, then all we need to find is what is the maximum profit that we can get in the [0, rightmost valid difficulty index] range. And to avoid calculating this for every worker, we can precomute this before we even apply Binary Search. 

But there is one issue with this approach and I was stuck at this for almost half an hour before I realised that I made a dumb mistake.

Notice that "difficulty" and "profit" are in sync. That means, ith difficulty has profit[i] profit. So if we only sort difficulty list, the profit list remains unchanged and that will not give us correct result. We cannot sort these two lists separately as well. Because profit of a job with a higher difficulty might be less than profit of a job with lower difficulty. So sorting them separately will also give wrong results.

And so, we want a way such taht when we sort the "difficulty" list, the "profit" list is still in sync. And for that, we can make a new list in which at every index, we have a pair of (difficulty, profit). So now, even if we sort this new list based on difficulty value, the profit value will always stay with its correct corresponding difficulty, just as it was initially in the input lists.

*You will find a lot of questions that have a similar pattern and they might differ in only the way we precompute max value. For some problems, you have to find maximum on right side whereas for some you have to find maximum on left side of each index. That depends on the problem statement. For example here, we know that if one difficulty is valid, all difficulties less than it are also valid. Hence we precomputed the maximum value on left side of each index.*