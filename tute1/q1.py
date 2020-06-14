

# You are given an array S of n integers and another integer x.
# (a) Describe an O(n log n) algorithm (in the sense of the worst case performance) that determines whether or not there exist two elements in S whose
# sum is exactly x.
# (b) Describe an algorithm that accomplishes the same task, but runs in O(n)
# expected (i.e., average) time.

class Solution:

	# a() implements the required solution with a worst case time complexity of 
	# O(n*logn) + O(n) = O(n*logn)
	def a(self, array, x):
		# edge case handling
		if not array:
			return False 

		if len(array) < 2:
			return False

		# sorting in python is nlogn in the worst case as it uses Timsort
		sortedA = sorted(array)
		lo, hi = 0, len(sortedA)-1

		# traverse throught the array and move according to the sum of pointers
		# this part of the solution will be O(n) as it is a single interation 
		# through the entire array in worst case
		while hi>lo:
			currSum = sortedA[lo] + sortedA[hi]
			if currSum == x:
				return True
			if currSum > x:
				hi -= 1
			elif currSum < x:
				lo += 1

		# if we reached the end of the array without finding the right elements
		# then the array does not contain such elements summing up to x
		return False

	# Solution b() provides an average case O(n) solutions through the usage of 
	# dictionaries (hash maps in python)
	def b(self, array, x):
		# edge case handling
		if not array:
			return False 

		if len(array) < 2:
			return False

		# begin solution
		complements = {}
		count = {}
		# we store the difference between each element to the target in the complements array. 
		# we also keep track of count of elements so we can utilise the same number twice if necessary 
		# and check against count dictionary
		for element in array:
			complements[element] = abs(x-element)
			count.setdefault(element, 0)
			count[element] += 1

		# for each complement, check whether it is in the array or the keys which represent array elements
		for key in complements:
			# if a key is the same as its complement then we might produce a false positive by reusing the same element
			# hence if count of that element is 
			if complements[key] in complements:
				if key == complements[key]:
					if count[key] > 1:
						return True
					else:
						continue

				return True

		return False


sol = Solution()
array = [1,2,-1]
print(sol.a(array, 0))
print(sol.b(array, 0))
