# Binary Search for the smallest index with value >= target
def binarySearch(citations, target, n):
    start = 0
    end = n - 1
    leftmostIndex = -1
        
    while start <= end:
        mid = start + (end - start) // 2
                
        if citations[mid] >= target:
            leftmostIndex = mid
            end = mid - 1
        else: start = mid + 1
            
    return leftmostIndex
    
    
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
        # This time, we will again use Binary Search here as well
        # We will try to find the index of smallest value that is >= mid
        # And in that way, n - index will be number of elements >= mid since array is sorted
        idx = binarySearch(citations, mid, n)
        count = n - idx if idx >= 0 else 0
            
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