
def platform(trainTimes):
	# store the arrival and departure times separately
	arrivals = []
	departures = []

	for time in trainTimes:
		arrival, departure = time[0], time[1]
		# if train arrives on previous day and leaves next day
		# split the arrival and departure times to treat as different trains
		# (arrival, 12 AM) and (12 AM, departure)
		# this wont affect the total count of trains at a given hour
		if arrival > departure:
			arrivals.append(0)
			departures.append(24)

		# ADD the arrival and departures to the consecutive lists
		arrivals.append(arrival)
		departure.append(departure)

	MergeSort(arrivals)
	MergeSort(departures)

	# keep track of minimum platforms required at a given time
	minPlatforms = 0
	# starting from the first departure to the last one
	for departureIndex in range(0, numDepartures):
		count = 0 
		# count the number of trains that arrived before this departure
		for arrival in arrivals:
			if arrival < departures[departureIndex]:
				count ++
			else:
				break

		# We get a tally of all trains that arrived before the departure time 
		# and then we remove the number of trains that have departed which is the current index
		platforms = count - index

		# The max platforms we need is the maximum number of trains we see at a given hour
		minPlatforms = max(trains, maxPlatforms)

	return minPlatforms



