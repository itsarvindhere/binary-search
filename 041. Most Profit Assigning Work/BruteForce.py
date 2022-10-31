def maxProfitAssignment(difficulty, profit, worker):
    
    maxProfit = 0
    
    m = len(worker)
    n = len(difficulty)
    
    # For every worker, find the maximum profit that he can get (if possible)
    for j in range (m):
        maxWorkerProfit = 0
        # Go through each job difficulty
        for i in range(n):
            # And if we find a difficulty <= ability of worker
            # Then we need to update the profit 
            # if this job gives a higher profit than previous job
            if difficulty[i] <= worker[j]:
                maxWorkerProfit = max(maxWorkerProfit, profit[i])
        
        # And when we found the maximum profit for this worker, just add it to the output that we need to return
        maxProfit += maxWorkerProfit
    
    
    return maxProfit

difficulty = [2,4,6,8,10]
profit = [10,20,30,40,50]
worker = [4,5,6,7]

print("Maximum Profit -> ", maxProfitAssignment(difficulty, profit, worker))