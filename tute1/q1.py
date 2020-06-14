

# You are given an array S of n integers and another integer x.
# (a) Describe an O(n log n) algorithm (in the sense of the worst case performance) that determines whether or not there exist two elements in S whose
# sum is exactly x.
# (b) Describe an algorithm that accomplishes the same task, but runs in O(n)
# expected (i.e., average) time.

class Solution:

	# a() implements the required solution with a worst case time complexity of 
	# O(n*logn) + O(n) = O(n*logn)
	def a(self, array, x):
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



sol = Solution()
ans = sol.a([1,2,3,65,43,-1,23,2], 100)
print(ans)
