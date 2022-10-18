# Helper method to find how many fractions are smaller than a particular fraction (target)
def countSmallerFractions(target, arr):
    count = 0
    p,q = 0,0
    maxFraction = 0
        
    for i in range(len(arr) - 1): 
        for j in range(i+1, len(arr)):
            # If for this jth element, fraction is <= target
            # That means, for any element after jth index also, this will be valid
            # hence we can simply increment count here
            if arr[i] / arr[j] <= target: 
                count += len(arr) - j
                    
                # If at the end, count is k, we need to return the pair
                # So here, we will also keep updating the pair values p and q
                if (arr[i] / arr[j]) > maxFraction: 
                    maxFraction = arr[i] / arr[j]
                    p = arr[i]
                    q  = arr[j]
                        
                break
                
                
    return (count, [p,q])
    
    
def kthSmallestPrimeFraction(arr, k):
        
    # Binary Search on Answer
    # We are asked for the Kth Smallest Prime Fraction
        
    # What can be the range of Fractions for this problem?
    # Since array is sorted in increasing order
    # and we consider a fraction where numerator < denominator
        
    # All valid fractions in the array will be between 0 and 1 only
    start = 0
    end = 1

    # Apply Binary Search
    # We want a fraction that is the kth smallest
    # In other words - There are k fractions less than or equal to it (including itself)
    while start < end:
            
        # We want the fraction, not an integer value
        # Hence we did not use "//" here
        mid  = start  + (end - start) / 2
                        
        # How many fractions are <= "mid" fraction
        (count, result) = countSmallerFractions(mid, arr)
                            
        if count == k: return result
            
        if count < k: start = mid
        else: end = mid
        
        
    return []




arr = [1,2,3,5]
k = 3

print("Kth Smallest Fraction -> ", kthSmallestPrimeFraction(arr, k))