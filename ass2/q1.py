# Given positive integers M and n compute Mn using only O(log n) many
# multiplications. (15 pts)


# DEF power(M , n):
# 	# Base case for the recursive function
# 	# RETURN 1 because anything to the power of 0 is 1
# 	IF n is ZERO:
# 		RETURN 1

# 	# Divide the number of power multiplications in HALF
# 	# Repeat the calculations
# 	temp = power(M, n/2)
# 	IF y is even:
# 		RETURN temp^2
# 	ELSE:
# 		RETURN (temp^2)*x






def power(x , y):
	if y == 0:
		return 1

	temp = power(x, int(y/2))
	if y%2 == 0:
		ans = temp*temp
	else:
		ans = temp*temp*x

	return ans


ans = power(3, 5)
print(ans)