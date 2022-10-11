def singleNonDuplicate(nums):
    
    # Since we are given a Sorted Array, this suggests that we can try Binary Search
    # Moreover, the problem asks us to have a O(LogN) solution
    # Which basically means, we are asked to use Binary Search to solve this problem.
    n = len(nums)
    start = 0
    end = n - 1
        
    while start <= end:
        mid = start + (end - start) // 2
            
        # If the mid index is even and duplicate is on its left
        condition1 = mid % 2 == 0 and nums[mid] == nums[mid - 1]
            
        # If the mid index is odd and duplicate is on its right
        condition2 = mid % 2 != 0 and nums[mid] == nums[mid + 1]
            
        # Search on left side of mid if either of two conditions is true
        if condition1 or condition2: end = mid - 1
        # Otherwise search on right side of mid
        else: start = mid + 1
                    
                    
    # In the end, the (start - 1) index will point to index of single element
    return nums[start - 1]

nums = [1,1,2,3,3,4,4,8,8]
print("Single Element is -> ", singleNonDuplicate(nums))