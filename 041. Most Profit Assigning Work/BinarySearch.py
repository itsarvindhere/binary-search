def maxProfitAssignment(difficulty, profit, worker):
        
        maxProfit = 0
        
        m = len(worker)
        n = len(difficulty)
        
        # We cannot just sort difficulty array
        # We also need to make sure profit array is in same order as difficulty array
        # So what we can do is at each index, we can keep what is the difficulty of a job and what is its profit
        jobs = []
        for i in range(n): jobs.append((difficulty[i], profit[i]))
            
        # Now we can sort this new list we made and since difficulty is the first value in each tuple
        # this list will be sorted based on difficulty
        jobs.sort()
        
        # Precompute maximum profit on left for each index
        maxProfitSoFar = [0] * n
        
        # For first index, maximum profit on left will be profit at its index only
        maxProfitSoFar[0] = jobs[0][1]
        for i in range(1, n): maxProfitSoFar[i] = max(maxProfitSoFar[i - 1], jobs[i][1])           

        # For every worker, find the maximum profit that he can get (if possible)
        for j in range(m):
            maxWorkerProfit = 0
            
            # Instead of linear search, we can now apply Binary Search here
            # As we have sorted the difficulty
            # Since difficulty is sorted, all we want to find is the rightmost valid index in difficulty array
            # That is the rightmost index at which difficulty is <= ability of the worker
            
            start = 0
            end = n - 1
            rightmostIndex = -1
            
            
            while start <= end:
                mid = start + (end - start) // 2
                
                # If job at mid can be done by worker
                # Then this is one possible solution
                # But we want rightmost valid difficulty
                # So we keep searching on right side of mid
                if jobs[mid][0] <= worker[j]:
                    rightmostIndex = mid
                    start = mid + 1 
                # If job at mid cannot be done by the worker
                # That means, no job after mid can be done as well
                # Since array is now sorted
                else: end = mid - 1
            
            # Now, as we have precomputed maximum profit till each index already
            # We can find the maximum profit till rightmostIndex in O(1) time
            if rightmostIndex != -1: maxWorkerProfit = maxProfitSoFar[rightmostIndex]
                
            # And append that to the final output that we need to return
            maxProfit += maxWorkerProfit
            
        
        return maxProfit

difficulty = [2,4,6,8,10]
profit = [10,20,30,40,50]
worker = [4,5,6,7]

print("Maximum Profit -> ", maxProfitAssignment(difficulty, profit, worker))