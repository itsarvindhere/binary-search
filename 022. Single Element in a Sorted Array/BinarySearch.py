def singleNonDuplicate(nums):
    # Since we are given a Sorted Array, this suggests that we can try Binary Search
    # Moreover, the problem asks us to have a O(LogN) solution
    # Which basically means, we are asked to use Binary Search to solve this problem.
    n = len(nums)
    start = 0
    end = n - 1
        
    while start <= end:
        mid = start + (end - start) // 2
            
        # If the mid index is even
        if mid % 2 == 0:
            # We can be sure that the single element is on left of mid
            # If the mid element has its duplicate on its left side
            if nums[mid] == nums[mid - 1]: end = mid - 1
            # Else, it means that single element is on right side of mid
            else: start = mid + 1
            
        # If the mid index is odd
        else:
            # We can be sure that the single element is on left of mid
            # If the mid element has its duplicate on its right side
            if nums[mid] == nums[mid + 1]: end = mid - 1
            # Else, it means that single element is on the right side of mid
            else: start = mid + 1
                    
                    
    # In the end, the (start - 1) index will point to index of single element
    return nums[start - 1]


nums = [1,1,2,3,3,4,4,8,8]
print("Single Element is -> ", singleNonDuplicate(nums))