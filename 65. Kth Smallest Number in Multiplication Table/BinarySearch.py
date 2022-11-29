# Helper method to find how many elements are smaller than "x"
def countSmaller(x, m, n):
    count = 0
        
    # Each row is like 
    # i*1, i*2, i*3........ i*n
        
    # Suppose there are "count" elements that are <= "x"
    # This means, i * count <= x
    # In other words, count <= x / i
    # So, count can be at most "x / i"
        
    # Hence, in each row, there are "x / i" elements smaller than "x"
    # For some test cases "x / i" might become > n
    # But since each row has "n" elements, if "x/i" becomes greater than n
    # That means, all elements of that row are <= x
    for i in range(1, m + 1): count += min(int(x / i), n)
    
    return count
                
    
def findKthNumber(m, n, k):
    # BINARY SEARCH ON ANSWER
        
    # THE SMALLEST NUMBER CAN BE 1
    # THE LARGEST POSSIBLE NUMBER CAN BE m*n
        
    start = 1
    end = m * n

    while start <= end:
        mid = start + (end - start) // 2
            
        # How many elements are smaller than "mid"
        count = countSmaller(mid, m, n)
        # If there are less than "k" elements smaller than "mid"
        # Then we cannot find the kth smallest on left side of "mid"
        # So in that case, we need to search on right side of mid
        if count < k: start = mid + 1
                
        # If there are "k" or more than "k" elements smaller than "mid"
        # Then we can find the kth smallest on left side of "mid"
        else: end = mid - 1
        
    return start

m,n,k = 3,3,5
print("Kth Smallest Number -> ", findKthNumber(m, n, k))