# ===================================================================================
# PART A
# ==================================================================================
# DEF squareSums(nums):
	
# 	# Store the squared values of given array in SQUARES
# 	squares= []

# 	# This FOR loop will iterate through all the elements in nums
# 	# The time complexity for this Loop will be O(n)
# 	FOR num in nums:
# 		Append num^2 to squares


# 	# We want to store all possible sums of pairs of square numbers
# 	allSums = []

# 	# This FOR loop will iterate through n, n-1, n-2, ... 1 elements
# 	# So in total, it will run n(n-1)/2 times
# 	# The time complexity for this Loop will be O(n^2)
# 	FOR i in range(0, length of squares array):
# 		FOR j in range(i, length of squares array):
# 			if i == j:
# 				continue 

# 			Add squares[i] + squares[j] to the allSums array



# 	# sort the allSums array containing sums of all possible pairs of squares
# 	# we apply merge sort for the shortest worst case time complexity of 
# 	# O(n*logn)

# 	sortedAllSums = MergeSort(allSums)


# 	# This FOR loop will iterate through all the elements in sortedAllSums
# 	# The time complexity for this Loop will be O(n^2)

# 	FOR element in sortedAllSums:
# 		IF element == next element:
# 			A number exists such that it can be written as a sum of 
# 			two distinct numbers in our array in two different ways
# 			RETURN True

# 	RETURN False
# ===================================================================================

# ===================================================================================
# PART B
# ===================================================================================
# DEF squareSums(nums):
	
# 	# Store the squared values of given array in SQUARES
# 	squares= []

# 	# This FOR loop will iterate through all the elements in nums
# 	# The time complexity for this Loop will be O(n)
# 	FOR num in nums:
# 		Append num^2 to squares


# 	# Store the count of occurrence of each sum in a hashmap 
# 	# sumCounts MAPS Sum -> Count
# 	sumCounts = {}

# 	# This FOR loop will iterate through n, n-1, n-2, ... 1 elements
# 	# So in total, it will run n(n-1)/2 times
# 	# The time complexity for this Loop will be O(n^2)
# 	FOR i in range(0, length of squares array):
# 		FOR j in range( i+1 , length of squares array):

# 			# Insert, Update and Get operations are O(1) in average case
# 			Increment the count of sum in sumCounts
# 			IF count of sum in sumCounts > 1:
# 				RETURN True

# 	Return False

# ===================================================================================

