def checkIfExist(arr):
    # For Each Element in the Array
    for i in range(len(arr)):
        # Go through each element
        for j in range(len(arr)):
            # Check if condition is met
            # If yes, return True
            if i != j and arr[i] == 2 * arr[j]: return True
    
    # If we come out of the first loop, that means, there is no such pair
    # Hence, return False
    return False


arr = [10,2,5,3]

print(checkIfExist(arr))