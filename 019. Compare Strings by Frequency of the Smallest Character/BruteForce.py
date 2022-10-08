# Function to return the frequency of lexographically smallest character
def f(s):  
    freq = 0
    smallest = s[0]
        
    # Find the frequency of smallest character
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
        
    # These arrays will have frequency of smallest character 
    # for each string in queries and words arrays
    queryFreq,wordFreq = [],[]
        
    for query in queries: queryFreq.append(f(query))
            
    for word in words: wordFreq.append(f(word))
        
    # Now using Brute Force, for each query, see how many words have a bigger frequency of smallest character
    for query in queryFreq:
        count = 0
        for word in wordFreq:
            if query < word: count += 1
        output.append(count)
                

    return output


queries = ["bbb","cc"]
words = ["a","aa","aaa","aaaa"]

print("Output -> ", numSmallerByFrequency(queries, words))