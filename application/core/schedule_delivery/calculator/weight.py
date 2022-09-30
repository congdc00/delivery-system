def sum_weight(target):
	trip = target.get_trip()
	weight = 0
	for turn  in trip:
		bound = turn.get_bound()
		weight += bound
	return weight