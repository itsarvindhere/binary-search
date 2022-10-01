def fairCandySwap(aliceSizes, bobSizes): 
    # Since we want to make sure both have same number of candies
    # Find how many candies each should have after the swap
    aliceSum = sum(aliceSizes)
    bobSum = sum(bobSizes)
        
    half = (aliceSum + bobSum) / 2
        
    # Sort the bobSizes list before applying binary search on it
    bobSizes.sort()
        
    # Binary Search
    # What are we searching for?
    # We want any value in bobSizes list such that that value + (aliceSum - value that alice will swap) should be equal to half
    for aliceVal in aliceSizes:
        start = 0
        end = len(bobSizes) - 1
            
        while start <= end:
            mid = start + (end - start) // 2
            bobVal = bobSizes[mid]
                
            if bobVal + (aliceSum - aliceVal) == half:
                return [aliceVal, bobVal]
                
            if bobVal + (aliceSum - aliceVal) < half:
                start = mid + 1
            else: end = mid - 1
        
    return []

aliceSizes = [1,2]
bobSizes = [2,3]
print("Output -> ", fairCandySwap(aliceSizes, bobSizes))