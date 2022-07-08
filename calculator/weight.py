def sum_weight(target):
	status = target.get_status()
	if status == 0:
		return 0
	else:
		return target.get_weight_delivered()