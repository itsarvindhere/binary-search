def hIndex(citations):
    # We know that h-index can be in the range 0 to number of citations
    # But instead of going through each possible "h-index" value i.e., linear search
    # We can use Binary Search since range of possible "h-index" values is in a sorted manner
        
    n = len(citations)
        
    start = 0
    end = n
    h = 0
        
    while start <= end:
        mid = start + (end - start) // 2
            
        # Find how many papers have at least "mid" citations
        count = 0
        for citation in citations:
            if citation >= mid: count += 1
            
        # If count is at least "mid" then "mid" is one possible h-index value
        # But we want to maximize the "h-index"
        # Hence, we will keep searching for a higher valid h=index value on right side of mid
        if count >= mid:
            h = mid
            start = mid + 1
        else: end = mid - 1
    return h


citations = [0,1,3,5,6]
print("H-index is -> ", hIndex(citations))