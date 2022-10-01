def missingNumber(nums):
    # To Apply Binary Search, we have to sort the given array first
    nums.sort()
        
    # What are we searching for?
    # We know that numbers are in the range 0 to n which means, at each index, number should be equal to index
    # e.g. at 0, number should be 0 and so on...
    # So for each mid position, we just need to check if at mid, the number is at its correct place or not.
    # Because the array is sorted, if mid is at correct place, all elements before it are also at correct place
        
    start,end = 0, len(nums) - 1
    missing = -1
        
    while start <= end:
        mid = start + (end - start) // 2
            
        # If the element at mid is not at its correct place
        # Either that index is the missing number or 
        # There is some missing number before that is causing this wrong placement
        # Hence, even after this condition is true, we won't stop searching.
        # We will search on left of mid if mid element is not at correct place
        # Else we will search on right of mid if mis is already at right place
        if nums[mid] != mid: 
            missing = mid
            end = mid - 1
        else: start = mid + 1
        
    # If at the end, missing number is still -1, that means it is n which is the length of the array
    # This is for Cases such as [0,1]
    return len(nums) if missing == -1 else missing


nums = [9,6,4,2,3,5,7,0,1]

print("Missing Number is -> ", missingNumber(nums))