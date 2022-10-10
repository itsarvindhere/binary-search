def twoSum(numbers, target):
    # The Brute Force approach will be -
    # For each number, try to find any number such that both add up to target
        
    for i1,num1 in enumerate(numbers):
        for i2,num2 in enumerate(numbers):
            if i2 > i1 and num1 + num2 == target:
                # Since 1-based indexing
                return[i1 + 1, i2 + 1]
        
    return []


numbers = [2,7,11,15]
target = 9
print("Solution -> ", twoSum(numbers,target))