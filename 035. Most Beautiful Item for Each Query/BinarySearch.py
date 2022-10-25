def maximumBeauty(items, queries):
    # Output Array to return
    output = [0] * len(queries)
        
    # Sort the items based on the price
    items.sort()
        
    # To perform binary search based on price
    # We need to ensure that at any index in items array
    # we can find what is the max beauty value till that index in constant time
    # So we can precompute the max beauty till any index
    for i in range(1, len(items)): items[i][1] = max(items[i][1], items[i-1][1])
        
        
    # Sort the queries as well
    # But since we also want their original indices
    # Convert each query into a tuple of (query, index) before sorting it
    queries = [(query, i)  for i, query in enumerate(queries)]
        
    # Sort the queries
    queries.sort()
        
    # The index at which we found maxBeauty for previous query
    # Initially, it will be the 0th index
    idx = 0

    for query, index in queries:
            
        # Now, instead of linear search, apply Binary Search
        start, end = idx, len(items) - 1
            
        while start <= end:
            mid = start + (end - start) // 2
                
            # If the price of item at mid is <= query
            # Then it can be one possible solution
            # But there may be an item after it with price <= query
            # So keep searching for that on right side of mid
            if items[mid][0] <= query:
                idx = mid
                output[index] = items[mid][1]
                start = mid + 1
            else: end = mid - 1
            
    return output



items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
queries = [1,2,3,4,5,6]

print("Output -> ", maximumBeauty(items, queries))