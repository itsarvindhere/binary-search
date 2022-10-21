from math import ceil
# Helper method to find if we can distribute all the products
# If "x" is the maximum products we can give to any store
def canDistribute(x, n, quantities):
        
    stores = 0
        
    for quantity in quantities:
        stores += ceil(quantity / x)
            
        # stores > n means there will be some products left that won't be distributed
        # But we want to distribute all products among "n" stores only
        # Hence, if this is the case, return False
        if stores > n: return False

    return True

    
def minimizedMaximum(n, quantities):
    # BINARY SEARCH ON ANSWER
    # We are asked to find the minimum "x"
    # Here, x => Maximum Products given to any store
        
    # What can be the valid range of x?
    # It is the range between the smallest possible "x" value and largest possible "x" value
    # A store can get at least 1 product
        
    # And the maximum products a store can get is the maximum value in the array
    # Because a store can only be given at most one product type
        
    start = 1
    end = max(quantities)
        
    res = float('inf')
        
    while start <= end:
            
        mid = start + (end - start) // 2
            
        # If "mid" is the maximum number of products given to a store
        # Can we distribute "all products"
        # If it is valid, this can be a possible result
        # But we want to minimize this value
        # Hence, keep searching on left side of mid
        if canDistribute(mid, n, quantities):
            res = mid
            end = mid - 1
        else: 
            start = mid + 1
        
    # At the end, return the minimized maximum
    return res

n = 7
quantities = [15,10,10]

print("Minimum Possible x is", minimizedMaximum(n, quantities))