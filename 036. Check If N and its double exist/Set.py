def checkIfExist(arr):
        
        # Set so that lookup is in constant time
        nums = set()
        
        for el in arr:
            # if the double of this element is present in set
            # Or its half is present in the set
            # Then we have a pair
            if el * 2 in nums or el / 2 in nums: return True
            
            # Otherwise, add this element to set and move to the next iteration
            nums.add(el)
            
    
        # If we come out of loop, that means, there is no valid pair at all
        return False


arr = [10,2,5,3]

print(checkIfExist(arr))