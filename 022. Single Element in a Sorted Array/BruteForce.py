def singleNonDuplicate(nums):
    # This approach is pretty straightforward
    # Since every element appears twice, except one.
    # it means, for every element, just check its next index. It should be the same element
        
    i = 0
    while i < len(nums) - 1:
        if nums[i] != nums[i + 1]: return nums[i]
        else: i += 2
        
        
    # If we haven't found the element yet, the last element is the required element
    return nums[-1]

nums = [1,1,2,3,3,4,4,8,8]
print("Single Element is -> ", singleNonDuplicate(nums))