def findPeakElement(nums):
        start, end = 0, len(nums) - 1
        
        minVal = float("-inf")
        
        while start <= end:
            mid = start + (end  - start) // 2
            
            # First or last element can be the peak as well
            # But in that case, the previous or next element won't be present in the list
            # So we can take previous and next as negative infinity
            prev = minVal if mid - 1 < 0 else nums[mid - 1]
            next = minVal if mid + 1 > len(nums) - 1 else nums[mid + 1]
            
            if nums[mid] > prev and nums[mid] > next: return mid
            
            # If mid element is not peak, then that means either the left side element is bigger
            # Or right side element is bigger
            # Whichever element is bigger among both, go towards that side
            if nums[mid - 1] > nums[mid]: end = mid - 1
            else: start = mid + 1
                
                
        return len(nums) - 1

nums = [1,2,1,3,5,6,4]

print("Index of peak element -> ", findPeakElement(nums))