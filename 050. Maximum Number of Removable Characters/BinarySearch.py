# Helper method to check if a particular "k" value is valid or not
def isValid(s,p,k,removable):
    # First remove the "k" characters from "s"
    # We need to remove characters at first "k" indices in removable
    iSet = set(removable[:k])
    newS = []
        
    # newS array will have only the characters that were not removed
    for i,char in enumerate(s): 
        if i not in iSet: newS.append(char)
        
        
    # Now we will try to find all the characters in "s" that are present in "p"
    # Since we will do it in one iteration, it will ensure that sequence is maintained
    count = 0
    index = 0
    for i,char in enumerate(newS):
        if p[index] == char: 
            index += 1
            count += 1
            
        # If count is same as the length of "p" it means "p" is still subsequence of "s"
        if count == len(p): return True
            
    # Otherwise, we can return False
    return False

    
def maximumRemovals(s, p, removable):
    # Binary Search on Answer
    # We want to find the maximum k
        
    # It is given that the range of "k" is from 0 to length of removable
    # And since this range is sorted, we can use Binary Search on this range
        
    start = 0
    end = len(removable)
    k = 0
        
    while start <= end:
        mid = start + (end - start) // 2
            
        # If after removing "mid" characters from "s" 
        # Using first "mid" indices in removable
        # If "p" is still a subsequence of "s"
        # Then "mid" is one possible value for maximum "k"
        # But since we want to maximize k, we will keep searching for a bigger value
        # That is, on the right side of mid
        if isValid(s, p, mid, removable):
            k = mid
            start = mid + 1
        else: end = mid - 1
        
    return k


s = "abcacb"
p = "ab"
removable = [3,1,0]

print("Maximum number of removable characters -> ", maximumRemovals(s, p, removable) )