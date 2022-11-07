# Binary Search for the first occurance of an element in a sorted list
def firstPosition(nums, target):
    start = 0
    end = len(nums) - 1
    firstPos = -1
        
    while start <= end:
        mid = start + (end - start) // 2
            
        # If at mid we find "target", then it could be the first occurance
        # But to be sure, we want to keep searching on left side of mid
        if nums[mid] == target: 
            firstPos = mid
            end = mid - 1
        elif nums[mid] > target: 
            end = mid - 1
        else: start = mid + 1
                
    return firstPos
    
    
# Binary Search for the last occurance of an element in a sorted list
def lastPosition(nums, target):
    start = 0
    end = len(nums) - 1
    lastPos = -1
        
    while start <= end:
        mid = start + (end - start) // 2
            
        # If at mid we find "target", then it could be the last occurance
        # But to be sure, we want to keep searching on right side of mid
        if nums[mid] == target: 
            lastPos = mid
            start = mid + 1
        elif nums[mid] > target: 
            end = mid - 1
        else: start = mid + 1
                
    return lastPos
 
def searchRange(nums, target):
    output = [-1,-1]
    firstPos = firstPosition(nums, target)
        
    # If first occurance is -1 that means the element is not at all in the array
    # So in that case, we can straight away return the array with -1 values
    if firstPos == -1: return output
        
    output[0] = firstPos
    output[1] = lastPosition(nums, target)
        
    return output


nums = [5,7,7,8,8,10]
target = 8

print("Output -> ", searchRange(nums,target))