'''
合并两个有序数组
'''


def merge_sorted_list(a_array, b_array):
	a_index, b_index = 0, 0
	a_length, b_length = len(a_array), len(b_array)
	
	if a_length == 0 or b_length == 0:
		return a_array + b_array
	new_sorted_list = list()
	
	while a_index < a_length and b_index < b_length:
		if a_array[a_index] <= b_array[b_index]:
			new_sorted_list.append(a_array[a_index])
			a_index += 1
		else:
			new_sorted_list.append(b_array[b_index])
			b_index += 1
	
	for item in (a_array[a_index:] + b_array[b_index:]):
		new_sorted_list.append(item)
	return new_sorted_list


a = [0, 1, 3, 5, 9]
a = []
# b = [2, 4, 6, 7]
b = []
b = [-1]
array = merge_sorted_list(a, b)
print(array)
