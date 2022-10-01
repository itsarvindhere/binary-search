def missingNumber(nums):
    xor = 0
        
    #First find the XOR of Indexes : o to n
    for i in range(0, len(nums) + 1): xor ^= i
            
    #And now find the XOR of numbers in the given array
    for num in nums: xor ^= num
            
    #Finally, XOR will be equal to the missing number
    return xor

nums = [9,6,4,2,3,5,7,0,1]

print("Missing Number is -> ", missingNumber(nums))