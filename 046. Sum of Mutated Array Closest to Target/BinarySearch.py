# Helper method to find the sum off array
# After replacing all elements larger than "x" with "x"
def getSum(x, arr, target):
    currSum = 0
            
    for num in arr: currSum += num if num < x else x
            
    return currSum
    
    
def findBestValue(arr, target):
    # What is the smallest possible "value"? It can be "1"
    # Since range of values in the array is from 1 to 10^4   
        
    # And similarly, what is the largest possible "value"? 
    # It is the max value in the array
    # because any value more than that will always give the same absolute difference
          
    # So we try to apply Binary Search on this range of 1 to max(arr) to find the required "value"
    # Because the range is in a sorted order
    start = 1
    end = max(arr)
        
    while start <= end:
        mid = start + (end - start) // 2
            
        # What is this mid?
        # This is a possible "value"
        # So we need to check if after changing all numbers > mid in the array to mid
        # The sum is equal to target or not
        currSum = getSum(mid, arr, target)
            
        # If the sum we get is same as target, it simply means this is the least possible absolute difference
        # Because the absolute difference between sum and target will be "0"
        # Hence we can simply return "mid" value
        if currSum == target: return mid
            
        # If the sum if still less than target, search on right of mid as we want a larger sum
        if currSum < target: start = mid + 1
                
        # If the sum becomes more than target, search on left of mid
        else: end = mid - 1
        
    # Here, "start" and "end" will be two values that will give us two closest absolute differences
    # So, we want the closest of the two values
    sum1 = getSum(start, arr, target)
    sum2 = getSum(end, arr, target) 
        
    diff1 = abs(sum1 - target)
    diff2 = abs(sum2 - target)
        
    # Since "end" is less than "start", this will take care of the condition of a "tie"
    return start if diff1 < diff2 else end


arr = [4,9,3]
target = 10

print("Output -> ", findBestValue(arr, target))