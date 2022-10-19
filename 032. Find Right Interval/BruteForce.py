def findRightInterval(intervals):
    output = []
    maxVal = float("inf")
        
    for i in range(len(intervals)):
        smallestStart  = maxVal
        index = -1
        for j in range(len(intervals)):
            if intervals[j][0] >= intervals[i][1]:
                if intervals[j][0] < smallestStart:
                    smallestStart =  intervals[j][0]
                    index = j
            
        output.append(index)
            
    return output

intervals = [[3,4],[2,3],[1,2]]

print("Output List is -> ", findRightInterval(intervals))