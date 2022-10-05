def peakIndexInMountainArray(arr):
    # We can try to apply Binary Search. How?
    # At each iteration, we check if mid index is the peak or not
        
    start = 0
    end = len(arr) - 1
        
    while start <= end:
        mid = start + (end - start) // 2
            
        # If this the peak index?
        if arr[mid-1] < arr[mid] and arr[mid + 1] < arr[mid]: return mid
            
        # If this is not the peak index, then we need to either move to left or right side
            
        # If element after the mid is bigger that means we can find a peak index on the right side of mid
        if arr[mid + 1] > arr[mid]: start = mid + 1
        # If element before the mid is bigger that means we can find a peak index on the left side of mid
        else: end = mid - 1
        
    return -1

arr = [0,1,0]

print("Peak Index is -> ", peakIndexInMountainArray(arr))
