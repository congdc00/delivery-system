import sys
from turtle import distance

from zmq import device

from config import NUM_DRONE, SPEED_TRUCK, WORKING_TIME

from calculator.weight import sum_weight
from calculator.distant import set_distant
from object.target import Target

def sum_fitness(population):
	result = 0
	count = 0
	min_fitness = 0
	for individual in population:
		count += 1
		fitness = individual.get_fitness()
		result += fitness
		min_fitness = min(min_fitness, fitness) 
	result += min_fitness*count
	return result, min_fitness

def sum_point(population):
	result = 0
	for individual in population:
		result += individual.get_point()
	return result


def get_fitness_and_point(list_target, list_device):

	penalty = 0
	
	max_point = 0
	max_weight = 0

	# tim khoi luong max de chuan hoa 
	for target in list_target: 
		weight = target.get_weight()
		max_weight = max(max_weight, weight)

	# phat ve khoi luong
	sum_point = 0
	for target in list_target:
		weight = target.get_weight()
		weight_deliver = sum_weight(target)
		lower_bound, upper_bound = target.get_bound_base()
		ratio = weight_deliver/upper_bound
		if weight_deliver < lower_bound:
			penalty -= ratio*weight

		if weight_deliver < upper_bound:
			sum_point += weight_deliver*weight
		else:
			sum_point += upper_bound*weight
	
		max_point += upper_bound*weight
	
	
	depot = Target(-1, 0, 0, 0,0,0)
	_,_,matrix_distance = set_distant(depot,list_target)
	# phat ve thoi gian
	speed_drone = list_device[0].get_speed()
	working_time = WORKING_TIME
	duration = list_device[0].get_duration()
	sum_time_device = []
	
	#kiem tra drone
	for id_device in range (0, NUM_DRONE):
		device = list_device[id_device]
		list_trip = device.get_trips()
		
		sum_time = 0
		# kiem tra thoi gian duration cua drone
		for trip in list_trip:
			distance = 0
			pre_point = -1

			if trip == []:
				break
			for turn in trip:
				id_target = turn.get_target()
				distance += matrix_distance[id_target+1][pre_point + 1]
				pre_point = id_target

			distance += matrix_distance[0][pre_point+1]
			time_limit_drone = 	distance/speed_drone
			
			if time_limit_drone < duration:
				penalty -= 0
			elif time_limit_drone > duration:
				penalty -= time_limit_drone/duration

			sum_time += time_limit_drone

		sum_time_device.append(sum_time)	

	
	# kiem tra truck
	
	for id_device in range(NUM_DRONE, len(list_device)):
		device = list_device[id_device]
		trip = device.get_trip()
		sum_time = 0
		distance = 0

		if trip == []:
			break
		
		pre_point = -1
		for turn in trip:
			id_target  = turn.get_target()
			distance += matrix_distance[id_target+1][pre_point+1]
			pre_point = id_target
			

		distance += matrix_distance[0][pre_point+1]
		sum_time = 	distance/SPEED_TRUCK
		
		sum_time_device.append(sum_time)
		
	# kiem tra working time
	# ? neu vi pham ve thoi gian thi cung phai danh vao loi nhuan (%tg vuot qua * loi nhuan dat duoc)
	for time in sum_time_device:
		if time < working_time:
			penalty -= 0

		elif time>working_time:
			penalty -= time/working_time
	if penalty == 0:
		fitness =  sum_point/max_point
	else:
		fitness =  penalty
	# danh penaty thoi gian cho drone, truck 
	# ty le penaty weght weght, timetimmett
	# 50 init_solution
	# education fc exchange 10 ( 1 khach trip nay sang trip kia); 20...; 11,21,
	# thuc hien tren § device
	# kich lowerbound target
	# 10K  100 0.5   
	return sum_point, fitness