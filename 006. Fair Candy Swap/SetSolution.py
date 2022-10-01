def fairCandySwap(aliceSizes, bobSizes):
        
    # Since we want to make sure both have same number of candies
    # Find how many candies each should have after the swap
    aliceSum = sum(aliceSizes)
    bobSum = sum(bobSizes)
        
    half = (aliceSum + bobSum) / 2
        
    aliceSet = set(aliceSizes)
        
    for bobVal in bobSizes:
        if bobVal + aliceSum - half in aliceSet:
            return [bobVal + aliceSum - half, bobVal]
        
        
    return []


aliceSizes = [1,2]
bobSizes = [2,3]

print("Output -> ", fairCandySwap(aliceSizes, bobSizes))
