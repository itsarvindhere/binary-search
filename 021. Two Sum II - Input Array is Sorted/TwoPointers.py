def twoSum(numbers, target):
        
    # Because the array is sorted, that means we can use two pointers
    # One will initially point at the start and other at end of array
    # And in each step, we check whether the two numbers at each pointers add up to target
    # If their sum is less than target, that means, we need to increase the left number
    # If their sum is more than target, that means, we need to decrease the right number
     
    start = 0
    end = len(numbers) - 1
        
        
    while start <= end:
        sum = numbers[start] + numbers[end]
            
        # If sum of two numbers is same as target, we found our pair
        if sum == target:
            return [start + 1, end + 1]
            
        # If sum is less than target, we need to incrase the left number
        if sum < target:
            start += 1
                
        # If sum is more than target, we need to decrease the right number
        else: 
            end -= 1
        
    return []


numbers = [2,7,11,15]
target = 9
print("Solution -> ", twoSum(numbers,target))