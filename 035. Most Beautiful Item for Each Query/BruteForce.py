def maximumBeauty(items, queries):
    output = []
        
    # In Brute Force Approach
    # We can go through each query        
    for target in queries:
        maxBeauty = 0 
        # And then loop through each item
        # To find the maximum beauty of an item
        # Whose price is <= query
        for i in range(len(items)): 
            if items[i][0] <= target: 
                maxBeauty = max(maxBeauty, items[i][1])
            
        output.append(maxBeauty)

    return output

items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
queries = [1,2,3,4,5,6]

print("Output -> ", maximumBeauty(items, queries))