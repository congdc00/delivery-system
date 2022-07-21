def sum_weight(target):
	list_trip = target.get_trip()
	weight = 0
	for trip in list_trip:
		weight += trip[1]
	return weight