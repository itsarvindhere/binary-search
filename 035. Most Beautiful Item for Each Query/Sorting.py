def maximumBeauty(items, queries):
    # Output Array to return
    output = [0] * len(queries)
        
    # Sort the items based on the price
    items.sort()
        
    # Sort the queries as well
    # But since we also want their original indices
    # Convert each query into a tuple of (query, index) before sorting it
    queries = [(query, i)  for i, query in enumerate(queries)]
        
    # Sort the queries
    queries.sort()
        
    # The index at which we found maxBeauty for previous query
    # Initially, it will be the 0th index
    idx = 0
        
    # The maxBeauty for previous query
    maxBeauty = 0
        
    for query, index in queries:
            
        # Instead of again looping from beginning of items list
        # We can start from where we left for previous query
        # Because queries are in sorted order
        for i in range(idx, len(items)):
            # If this item has price more than query, break
            if items[i][0] > query: break
                    
            # Otherwise, set maxBeauty to the maximum of previous and current beauty value
            maxBeauty = max(maxBeauty, items[i][1])
                
            # Also increment this variable
            # It is used to keep track of the index till which we iterated for the current query
            # So that for the next query, we start the loop from this index, instead of from the beginning
            idx += 1
                    
        output[index] = maxBeauty
            
    return output



items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
queries = [1,2,3,4,5,6]

print("Output -> ", maximumBeauty(items, queries))