# Helper method to check how many elements are smaller than a given element
def countSmaller(target, matrix, n):
    count = 0
    for row in range(n):
            
        # If first element itself is larget than target, skip that row
        if matrix[row][0] > target: continue

        # Binary Search instead of Linear Search
        # For each row, count how many elements are <= target
        start = 0
        end = n - 1
            
        while start <= end:
            mid = start + (end - start) // 2
                
            if matrix[row][mid] <= target: 
                start = mid + 1
            else: end = mid - 1
            
        count += start
                
    return count
    
    
def kthSmallest(matrix, k):
    # Binary Search on Answer
    # The smallest value of k can be 1 i.e., The smallest element
    # So lower bound is the element at row 0 and col 0
    # Similalry, the largest value of k can be n*n i..e, The largest element
    # So upper bound is the element at last row and last column
        
    n = len(matrix)
    start = matrix[0][0]
    end = matrix[n-1][n-1]
        
    # Apply Binary Search on this range
    while start <= end:
        mid = start + (end - start) // 2
            
        # Count of elements that are less than mid in the matrix
        count = countSmaller(mid, matrix, n)
            
        # IF number of elements smaller than mid are less than k 
        # That means we can never find kth smallest on left of mid
        if count < k: start = mid + 1
        # If number of elements smaller than mid are more than k
        # That means, kth smallest is on the left side of mid
        else: end = mid - 1
                
                
    return start


matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8

print("Kth smallest element is -> ",kthSmallest(matrix, k))