
def sum_weight(target):
	status = target.get_status()
	if status == 0:
		return 0
	else:
		return target.get_weight_delivered()

def sum_fitness(population):
	result = 0
	for individual in population:
		result += individual.get_fitness()

	return result
	
def get_fitness_and_point(list_target):

	point = 0
	all_weight = 0
	lower_bound,upper_bound = list_target[0].get_bound_base()

	for target in list_target:
		weight = target.get_weight()
		weight_deliver = sum_weight(target)
		if weight_deliver == 0:
			point -= 5*weight
		elif weight_deliver < lower_bound:
			point -= 2*weight
		elif weight_deliver < upper_bound:
			point -= 1*weight
		else:
			point += 1*weight

		all_weight += weight_deliver
	fitness =  all_weight*weight + point
	count_point = all_weight*weight
	# danh penaty thoi gian cho drone, truck 
	# ty le penaty weght weght, timetimmett
	# 50 init_solution
	# education fc exchange 10 ( 1 khach trip nay sang trip kia); 20...; 11,21,
	# thuc hien tren § device
	# kich lowerbound target

	#10K  100 0.5   
	return count_point, fitness