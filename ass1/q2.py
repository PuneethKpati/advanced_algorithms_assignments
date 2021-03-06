

# Recursive quick sort algorithm
# nuts : [3, 1, 5, 2, 6, 4]
# bolts: [5, 6, 2, 4, 1, 3]


# function quickPair(nuts, bolts):
# 	hashmap maps Nut-> Bolt
#   if nuts and bolts only have one element left in them:
#		hashmap[nuts[0]] = bolts[0] 
#   
# 	pivotNut = nuts[0]

#	This loop will be O(n) as we only iterate through bolts once
# 	for bolt in bolts:
# 		if bolt is smaller than pivotNut:
# 			add bolt to smaller
# 		elif bolt is bigger than pivotNut:
# 			add bolt to bigger
# 		if bolt fits pivot nut:
# 			pivotBolt = bolt 
# 			hashmap[pivotNut] = pivotBolt

#   This loop will be O(n) as we only iterate through nuts once
# 	for nut in nuts:
# 		if doesn't fit in pivotBolt:
# 			append nut to smallerNuts
# 		else:
# 			append nut to biggerNuts


# 	quickPair(smallerNuts, smallerBolts, hashmap)
# 	quickPair(biggerNuts, biggerBolts, hashmap)

# 	return hashmap

# We see that a single call to this function is O(n) + O(n) = O(2n) = O(n)
# We essentially divide the array everytime and each segment takes O(n) so we get 
# O(logn) * O(n) = O(n*logn)
# This function is also derived from the quicksort algorithm with no extra overhead 
# so, that adds to the proof that this function will run in expected time of O(nlogn). 
# However, in the worst case (nuts already ordered ascending or descending)
# it will run in O(n^2). 



def quickPair(nuts, bolts, pairs):
	# Edge case handling
	if not nuts or not bolts:
		return None 

	if len(nuts) == 0 or len(bolts)==0:
		return

	# final base case where only one nut and bolt are left
	if len(nuts) == 1 or len(bolts)==1:
		pairs[nuts[0]] = bolts[0]
		return pairs

	# select the first element of the nut as the pivot erlement 
	pivotNut = nuts[0]

	# lists to hold the nuts and bolts that are going to be divided
	smallerNuts, biggerNuts = [], []
	smallerBolts, biggerBolts = [], []

	# iterate through all bolts
	# this will be O(n) in terms of time complexity
	for bolt in bolts:
		if bolt < pivotNut:
			smallerBolts.append(bolt)
		if bolt > pivotNut:
			biggerBolts.append(bolt)
		elif bolt == pivotNut:
			pairs[pivotNut] = bolt
			pivotBolt = bolt

	# iterate through all nuts to divide them into smaller and larger 
	# this will be O(n) in terms of time complexity
	for nut in nuts:
		if nut < pivotBolt:
			smallerNuts.append(nut)
		elif nut > pivotBolt:
			biggerNuts.append(nut)

	# run the smaller and bigger sized nuts and bolts through the 
	# pairing function again
	quickPair(smallerNuts, smallerBolts, pairs)
	quickPair(biggerNuts, biggerBolts, pairs)

	# return the hashmap with all the pairings at the current level
	return pairs


nuts = [2, 1]
bolts = [1, 2]
pairs = quickPair(nuts, bolts, {})
print(pairs)



