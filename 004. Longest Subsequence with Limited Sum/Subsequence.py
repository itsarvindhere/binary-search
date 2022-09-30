def answerQueries(nums, queries):
    output = []
        
    # First Sort the given array
    nums.sort()
        
    n = len(nums)
        
    # Prefix Sum
    for i in range(1, n): nums[i] += nums[i - 1]
        
    # Each Query is a target sum
    # So, we want to find the largest Subsequence  with sum <= query
    for query in queries:
        start = 0
        end = n - 1
            
        result = -1
            
        while start <= end:
            mid = start + (end - start) // 2
                
            # If the sum at mid is <= query, this is one possible solution
            # WE want the longest Subsequence so we will continue searching by making start = mid + 1
            # E.g. what if after mid we have some 0s. That would result in same sum but size of subsequence will be larger than before
            if nums[mid] <= query:
                result = mid
                start = mid + 1
            else:
                end = mid - 1
            
        output.append(result + 1)
        
    return output


nums = [4,5,2,1]
queries = [3,10,21]

print("Result -> ", answerQueries(nums, queries))