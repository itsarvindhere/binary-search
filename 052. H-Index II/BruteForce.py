def hIndex(citations):
    # We know that h-index can be in the range 0 to number of citations
    # So, we will try to check each possible h-index value to see which one is maximum valid h-index
    h = 0
    n = len(citations)
        
    # For every possible h-index value "i"
    for i in range(n + 1):
        # Find how many papers have at least "i" citations
        count = 0
        for citation in citations:
            if citation >= i: count += 1
            
        # If count is at least "i" then "i" is one possible h-index value
        if count >= i: h = i
            
    return h

citations = [0,1,3,5,6]
print("H-index is -> ", hIndex(citations))