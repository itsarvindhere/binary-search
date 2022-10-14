# Helper method to check if an element is peak element or not
def isPeak(mat, row, col, m, n):
    # Check if it is greater than left neighbor
    if col > 0 and not (mat[row][col] > mat[row][col - 1]): return False
                
    # Check if it is greater than right neighbor
    if col < n - 1 and not (mat[row][col] > mat[row][col + 1]): return False
                    
    # Check if it is greater than top neighbor
    if row > 0 and not (mat[row][col] > mat[row - 1][col]): return False
                    
    # Check if it is greater than bottom neighbor
    if row < m - 1 and not (mat[row][col] > mat[row + 1][col]): return False
                    
    # If we are here, then this means, this element is the peak element
    return True
    
    
    
def findPeakGrid(mat):  
    m = len(mat)
    n = len(mat[0])
        
    for row in range(m):
            
        # Handling some edge cases
            
        # Is the first element peak?
        if isPeak(mat, row, 0, m, n): return [row, 0]
            
        # Is the last element peak?
        if isPeak(mat, m - 1, n - 1, m, n): return [m-1, n-1]
            
            
        # For each row, perform Binary search for the peak element
        # To reduce the complexity from O(mn) to O(mlogn)
        start = 0
        end = n - 1
            
        while start <= end:
            mid = start + (end - start) // 2
                
            # Check if mid element is the peak element or not
            if isPeak(mat, row, mid, m, n): return [row, mid]

            isSmallerThanLeft = mid > 0 and mat[row][mid] < mat[row][mid - 1]
            isSmallerThanRight = mid < n - 1 and mat[row][mid] < mat[row][mid + 1]
                
            # If it is smaller than both left and right side elements, move towards the bigger of two
            if isSmallerThanLeft and isSmallerThanRight:
                if mat[row][mid - 1] > mat[row][mid + 1]: end = mid - 1
                else: start = mid + 1
                
            # If it is smaller than left side element, then left element might be peak
            elif isSmallerThanLeft: end = mid - 1
                    
            # If it is smaller than right side element, then right element might be peak
            elif isSmallerThanRight: start = mid + 1
                    
            # If none of above cases is true, that means, mid is not peak because element on bottom is bigger
            # So we have a better chance to find a peak element in next row. So break
            else: break 



mat = [[1,4],[3,2]]
print("Peak Element Position is -> ", findPeakGrid(mat) )