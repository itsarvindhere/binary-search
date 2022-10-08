# Function to return the frequency of lexographically smallest character
def f(s): 
        
    freq = 0
    smallest = s[0]
        
    # In same loop, not just update the count but also keep track of smallest character
    for c in s: 
        # If we get a smaller character, update smallest and reset freq to 1
        if ord(c) < ord(smallest): 
            smallest = c
            freq = 1
            
        # If we get the same character as smallest, increment frequency
        elif ord(c) == ord(smallest): freq += 1
                
        # If we get a character bigger than smallest, skip
        else: continue
            
        
    # Return the frequency of smallest character
    return freq
        

def numSmallerByFrequency(queries, words):
    output = []
        
    queryFreq,wordFreq = [],[]
        
    for query in queries: queryFreq.append(f(query))
    for word in words: wordFreq.append(f(word))
            
    # Sort the words array
    wordFreq.sort()
        
    n = len(wordFreq)
        
    for query in queryFreq:
        count = 0
        # Apply Binary Search instead of Linear Search
        start, end = 0, n - 1
            
        while start <= end:
            mid = start + (end - start) // 2
                
            # If the mid word has a bigger frequency of smallest character
            # It is one possible solution
            # But there might be a word on left of mid that also satisfies this condition
            # So keep searching on left
            if wordFreq[mid] > query:
                count = n - mid
                end = mid - 1
            # Else search on right of mid as left of mid has all the words with smaller frequency
            else:
                start = mid + 1
                    
        output.append(count)

    return output


queries = ["bbb","cc"]
words = ["a","aa","aaa","aaaa"]

print("Output -> ", numSmallerByFrequency(queries, words))