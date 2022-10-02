def findKthPositive(arr, k):
    count = [0] * 1001
        
    # First count the occurance of each element in array
    for num in arr: count[num] += 1
        
    temp = k
    for i in range(1, arr[-1] + 1):
        # If i occurs 0 times that means it is not present
        # So decrement temp by 1
        if count[i] == 0: temp -= 1
            
        # If temp becomes 0, that means we found the kth missing positive
        if temp == 0: return i
            
    # If the missing number is greater than the last number of given array     
    return len(arr) + k

arr = [2,3,4,7,11]
k = 5

print("Kth Missing Positive Number is -> ", findKthPositive(arr,k))