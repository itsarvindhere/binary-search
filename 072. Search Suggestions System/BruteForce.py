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

		# And now, we want the matching words that have this prefix
		for word in products:

			# If prefix is the same, the word matches
			# So, we put the word in the matchedWords list
			if word[:i+1] == prefix: matchedWords.append(word)

			# If we already have three search results, break
			if len(matchedWords) == 3: break

		# And we can put the matchedWords in the output list
		output.append(matchedWords)

	# Return the output
	return output


products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"

print("Output -> ", suggestedProducts(products, searchWord))

