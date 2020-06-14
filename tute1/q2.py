
# QUESTION 2:
# ======================================================================================== 
# Given two arrays of n integers, design an algorithm that finds out in O(n log
# (n)) steps if the two arrays have an element in common. (Microsoft interview
# question
#
# ========================================================================================

class Q2:

	# The main approach for this solution is to sort both arrays 
	# and then simply traverse through them to find a common element
	def intersection(self, array1, array2):
		# edge case handling
		if not array1 or not array2:
			return None

		if len(array1) < 1 or len(array2) < 1:
			return False

		# sort both arrays, this will be O(nlogn) in worst case
		# because the python sorted() function uses TimSort 
		sorted1 = sorted(array1)
		sorted2 = sorted(array2)

		# store the lengths so you dont have to create new system calls everytime
		len1 = len(sorted1)
		len2 = len(sorted2)
		
		# use two pointers, one for each array
		# if an element in array 1 is greater than the pointed element in array2, then
		# move down in array2 to find a value equal to it. Keeo doing this vice-versa
		# if either index crosses the length of array then we couldnt find anything
		index1, index2 = 0, 0
		while index1 < len1 and index2 < len2:
			if sorted1[index1] == sorted2[index2]:
				print(sorted1[index1], sorted2[index2])
				return True

			if sorted1[index1] > sorted2[index2]:
				index2 += 1
			else:
				index1 += 1

		return False

q = Q2()
print(q.intersection([1,2,325,23,1,34,5], [12,3457,89,5645721]))