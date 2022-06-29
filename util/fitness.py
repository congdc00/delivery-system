
def count_weight(target):
	sum_weight = 0
	for trip in target:
		sum_weight += trip[1]

	return sum_weight

def sum_fitness(population):
	result = 0
	for individual in population:
		result += individual.get_fitness()

	return result
	
def get_fitness_and_point(list_target_base, list_target_result):

	point = 0
	sum_weight = 0
	lower_bound,uper_bound = list_target_base[0].get_bound_base()

	for i in range (0,len(list_target_result)):
		target = list_target_result[i]
		weight = list_target_base[i].get_weight()
		weight_deliver = count_weight(target)
		if weight_deliver == 0:
			point -= 5*weight
		elif weight_deliver < lower_bound:
			point -= 2*weight
		elif weight_deliver < uper_bound:
			point -= 1*weight
		else:
			point += 1*weight

		sum_weight += weight_deliver
	return sum_weight*weight, sum_weight*weight + point, 