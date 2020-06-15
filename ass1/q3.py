
import random

class Node:
	def __init__(self, right, left, bigger):
		self.bigger = bigger
		self.right = right
		self.left = left

	def __str__(self):
		return f'{self.bigger}\n{self.left} {self.right}\n'

def buildTree(array):
	if len(array) == 1:
		return array[0]

	layer = []
	for i in range(0,len(array)-1, 2):
		if array[i].val > array[i+1].val:
			layer.append(Node(array[i], array[i+1], array[i].val))
		else:
			layer.append(Node(array[i], array[i+1], array[i+1].val))

	return buildTree(layer)

array = []
for i in range(2**10):
	array.append(Node(None, None, i))
random.shuffle(array)

print(array)
root = buildTree(array)
print(root)



