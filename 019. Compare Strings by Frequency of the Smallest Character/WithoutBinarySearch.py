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

            
        
    # Return the frequency of smallest character
    return freq
        

def numSmallerByFrequency(queries, words):
        
    # Output array to return
    output = []
        
    # We are given that the maximum length of any string in any of two arrays is 10
    # What that means? It means that the freq of smallest character for any string is in range 1 to 10
    # That is, either there is only one smallest character, or all the characters are the same
        
        
    # So we can keep track of how many words in words array have same frequency of the smallest character
    # For that, we can use a constant sized array of length 11
    freqCount = [0] * 11
        
        
    # For example, if we have words = ["a","aa","aaa","aaaa"]
    # Here, for "a", freq of smallest is 1
    # For "aa", freq is 2 and so on..
        
    # So freqCount will be like - [0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
    
    # Each index = frequency of smallest character
    # At index = 1, we have value = 1. 
    # This means, there is only 1 word with frequency of smallest character = 1
    # Similarly, there is only 1 word with  frequency of smallest character = 2

    for word in words:
        freq = f(word)
        freqCount[freq] += 1
            
    # Now find the prefix sum
    # So that each index value then shows how many words are there with freq of smallest character <= index
    for i in range(1, len(freqCount)): freqCount[i] += freqCount[i - 1]
        
    # Now, we loop through each query
    for query in queries:
        freq = f(query)
        # Now, just find words with freq of smallest > freq
        # We can find that as -> Words with freq of smallest <= 10 - Words with freq of smallest <= freq
        output.append(freqCount[10] - freqCount[freq])

    return output


queries = ["bbb","cc"]
words = ["a","aa","aaa","aaaa"]


print("Output -> ", numSmallerByFrequency(queries, words))