# Helper Method for Binary Search
def binarySearch(i, products, prefix, isLeftIndexSearch):
    start,end = 0, len(products) - 1
            
    # Index of the leftmost (or rightmost) matching word in the products list
    idx = -1
            
    # Binary Search
    while start <= end:
                
        # Mid
        mid = start + (end - start) // 2
                
        # If the word at "mid" index matches
        # It may be the leftmost or rigtmost valid index
        # But to be sure, we will keep search on left or right side of mid
        if products[mid][:i + 1] == prefix: 
            idx = mid
            if isLeftIndexSearch: end = mid - 1
            else: start = mid + 1
                
        # If the word at "mid" doesn't match
        # Is the prefix at mid smaller than "prefix"?
        # In that case, search on right side of mid
        # Since on left, we cannot find any matching word at all
        elif products[mid][:i + 1] < prefix: start = mid + 1
                    
        # Otherwise if the prefix at mid is greater than "prefix"
        # Then search on left side of mid
        else: end = mid - 1
                
    # Return the required index
    return idx


def suggestedProducts(products, searchWord):

	# Length of the searchWord
        n = len(searchWord)
        
        # Output to return
        output = []
        
        # Sort the input list so that the products are in lexicographical order
        products.sort()
        
        # Now, we will go through each prefix
        for i in range(n):
            # Prefix
            prefix = searchWord[:i+1]
            
            # List to keep the matched words
            matchedWords = []
            
            # The reason for O(N^2) time complexity is the nested loop
            # In the inner loop, we have to loop over the entire list to search for matching products
            # But, since the list is already in sorted order, there is no need for a linear scan
            # We can use Binary Search
            
            # We want the leftmost valid index that matches the prefix
            # And the rightmost valid index the matches the prefix
            # So, all the words in between will be the matching words

            # Index of the leftmost matching word in the products list
            leftmostValidIndex = binarySearch(i, products, prefix, True)
            
            # If the leftmost valid index is -1, then there are no matching words
            if leftmostValidIndex == -1: 
                output.append(matchedWords)
                continue
            
            # Index of the rightmost matching word in the products list
            rightmostValidIndex = binarySearch(i, products, prefix, False)
            
            # Since we only want the three matching words
            matchedWords = products[leftmostValidIndex: min(leftmostValidIndex + 3, rightmostValidIndex + 1)]

            # Put the matchedWords in the output list
            output.append(matchedWords)
        
        # Return the output
        return output


products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"

print("Output -> ", suggestedProducts(products, searchWord))

