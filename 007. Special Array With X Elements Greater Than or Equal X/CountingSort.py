def specialArray(nums) :
        
    # Since the max value of any element in the array can be 1000
    count = [0] * 1001
        
    # Store the count of each element
    for num in nums: count[num] += 1
            
    # n is initially equal to total number of elements in the array
    # n = how many elements are equal to any x value in range 0 to n
    n = len(nums)
        
    # x can be in range 0 to n (inclusive)
    for x in range(0, n + 1):
        # We start with n = length of nums 
        # because for 0, numbers >= 0 is equal to length of array
        if x == n: return x
        # Before moving to next x, substract the count of numbers == current x
        n -= count[x]

    # If not a special array
    return -1


nums = [0,4,3,0,4]
print("Output ->", specialArray(nums))