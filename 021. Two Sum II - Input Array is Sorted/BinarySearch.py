def twoSum(numbers, target):
    # Since it is given that array is already sorted, why not use Binary Search
    # For each number, we want to find a second number such that it is equal to target - firstNumber
    # And that is something we can do using Binary Search
        
    for i1,num1 in enumerate(numbers):
        # Range is from the index after i1 to last index
        start = i1 + 1
        end = len(numbers) - 1
            
        while start <= end:
            mid = start + (end - start) // 2
                
            # If number at mid is the number we are looking for
            if numbers[mid] == target - num1:
                return [i1 + 1,mid + 1]
                
            # If the number at mid is less than target - num1
            # That basically means, we need to find a larger number
            # So look at right side of mid
            if numbers[mid] < target - num1:
                start = mid + 1
                    
            # Otherwise search on left side of mid
            else:
                end = mid - 1
                
        return []


numbers = [2,7,11,15]
target = 9
print("Solution -> ", twoSum(numbers,target))