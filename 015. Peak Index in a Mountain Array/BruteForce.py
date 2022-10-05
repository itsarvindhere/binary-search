def peakIndexInMountainArray(arr):
    # We go through each index, starting from the beginning 
    # And check if that index is peak or not
    # If it is peak, return from there
    for i in range(1, len(arr) - 1):
        if arr[i-1] < arr[i] and arr[i + 1] < arr[i]: 
            return i
           
    return -1


arr = [0,1,0]
print("Peak Index is -> ", peakIndexInMountainArray(arr))