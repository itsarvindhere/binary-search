def singleNonDuplicate(nums):
    # Since XOR of two same numbers is 0, it means if we XOR all the numbers in array
    # Eventually, we will get the number that is not occuring twice
        
    result = 0
        
    # XOR every number in the array
    for num in nums: result ^= num
        
    # The final value will be the required single element
    return result


nums = [1,1,2,3,3,4,4,8,8]
print("Single Element is -> ", singleNonDuplicate(nums))