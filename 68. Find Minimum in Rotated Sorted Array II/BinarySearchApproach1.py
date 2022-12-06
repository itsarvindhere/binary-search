def findMin(nums):
    # To remove the duplicates but keep the order
    nums = list(dict.fromkeys(nums))

    minimum = nums[0]

    n = len(nums)

    # We can search for the minimum element using Binary Search
    start = 0
    end = n - 1

    while start <= end:
        # If the "start" element is smaller than "end"
        if nums[start] < nums[end]: return min(minimum, nums[start])

        mid = start + (end - start) // 2

        # IF this mid value is smaller than previous minimum we found
        # Then update the minimum
        minimum = min(minimum, nums[mid])

        # Is this "mid" value part of left sorted subarray or right sorted subarray?
        # If this is part of the left sorted subarray, we will find minimum on right side
        if nums[mid] >= nums[start]: start = mid + 1
        # Otherwise, we will find the minimum on the left side
        else: end = mid - 1
        
    return minimum

nums = [3,3,0,1]

print("Minimum is -> ", findMin(nums))