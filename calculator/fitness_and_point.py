import sys

sys.path.append('/Users/dinhchicong/Project/scheduled-delivery')

from calculator.weight import sum_weight

def sum_fitness(population):
	result = 0
	for individual in population:
		result += individual.get_fitness()

	return result

def sum_point(population):
	result = 0
	for individual in population:
		result += individual.get_point()
	return result
	
def get_fitness_and_point(list_target):

	penalty = 0
	all_weight = 0
	lower_bound,upper_bound = list_target[0].get_bound_base()

	for target in list_target:
		weight = target.get_weight()
		weight_deliver = sum_weight(target)
		if weight_deliver == 0:
			penalty -= 5*weight
		elif weight_deliver < lower_bound:
			penalty -= 2*weight
		elif weight_deliver < upper_bound:
			penalty -= 1*weight
		else:
			penalty += 1*weight

		all_weight += weight_deliver
	fitness =  all_weight*weight + penalty
	count_point = all_weight*weight
	# danh penaty thoi gian cho drone, truck 
	# ty le penaty weght weght, timetimmett
	# 50 init_solution
	# education fc exchange 10 ( 1 khach trip nay sang trip kia); 20...; 11,21,
	# thuc hien tren § device
	# kich lowerbound target

	#10K  100 0.5   
	return count_point, fitness