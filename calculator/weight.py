def sum_weight(target):
	list_trip = target.get_trip()
	weight = 0
	for turn  in list_trip:
		bound = turn.get_bound()
		weight += bound
	return weight