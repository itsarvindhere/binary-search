def isBadVersion(n) :
    return n >= 20


def firstBadVersion(n):
    # Because the range 1 to n is in a sorted order
    # Why not use Binary Search?
        
    start = 1
    end = n
    firstBad = -1
        
    while start <= end:
        mid = start + (end - start) // 2
        # If mid version is bad, that is one possible answer
        # Maybe there are bad versions before this mid
        # So save the current mid version and keep searching on the left of mid
        if isBadVersion(mid):
            firstBad = mid
            end = mid - 1
        # If mid version is not bad, no version before it is bad
        # Hence, search on the right of mid
        else:
            start = mid + 1
        
    return firstBad

n = 100
print("First Bad Version is -> ", firstBadVersion(n))    