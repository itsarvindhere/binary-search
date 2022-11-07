# Binary Search for the first or last occurance of an element in a sorted list
def getPosition(nums, target, isFirst):
    start = 0
    end = len(nums) - 1
    pos = -1
        
    while start <= end:
        mid = start + (end - start) // 2
            
        # If at mid we find "target", then it could be the first/last occurance
        # But to be sure, we want to keep searching on left/right side of mid
        if nums[mid] == target: 
            pos = mid
            if isFirst: end = mid - 1
            else: start = mid + 1
        elif nums[mid] > target: 
            end = mid - 1
        else: start = mid + 1
                
    return pos

def searchRange(nums, target):
    output = [-1,-1]
    firstPos = getPosition(nums, target, True)
        
    # If first occurance is -1 that means the element is not at all in the array
    # So in that case, we can straight away return the array with -1 values
    if firstPos == -1: return output
        
    output[0] = firstPos
    output[1] = getPosition(nums, target, False)
        
    return output


nums = [5,7,7,8,8,10]
target = 8

print("Output -> ", searchRange(nums,target))