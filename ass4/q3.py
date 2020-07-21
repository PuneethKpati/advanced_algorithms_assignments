# QUESTION
# ==================================================================================
# You are on vacation for N days at a resort that has three possible activities.
# For each day, for each activity, you’ve determined how much enjoyment you
# will get out of that activity. However, you are not allowed to do the same
# activity two days in a row. What is the maximum total enjoyment possible?
# ==================================================================================

class Q3:
	def maxEnjoyment(days):
		# If we are at the first day the return
		# the enjoyment scores for that day
		if len(days) == 1:
			return days[0]

		# FunToday has the enjoyment scores for today 
		FunToday = days[-1]
		# FunTillToday recyrsively finds the maximum 
		# enjoyment we could have had till the current day
		FunTillToday = Q3.maxEnjoyment(days[:-1])

		# store the max enjoyment scores for today in maxFun
		maxFun = []
		# For EACH activity find the maximum fun by 
		# summing today's score with the most optimal choice from yesterday\
		temp = 0
		for activityNum in range(3):
			temp = FunToday[activityNum]
			# add the optimal activity choice by finding maximum enjoyment
			temp += max( FunTillToday[(activityNum+1)%3], FunTillToday[(activityNum+2)%3] )
			maxFun.append(temp)

		# return the values of maximum enjoyment values
		return maxFun


days = [
[1,2,1],
[3,2,4],
[6,3,2],
[12,5,2]
]

solution = Q3.maxEnjoyment(days)
print(solution)