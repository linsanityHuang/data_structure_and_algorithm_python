'''
找出数组中前k个最小的元素
'''


def find_mini_k(input_array, k):
	n = len(input_array)
	if k >= n:
		return input_array
	
	pivot = input_array[k]
	extra_array = input_array[:k] + input_array[k:]
	less = [x for x in extra_array if x <= pivot]
	great = [x for x in extra_array if x > pivot]
	
	pass
