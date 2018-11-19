import numpy as np


def quick_sort(input_array):
	n = len(input_array)
	if n <= 1:
		return input_array
	
	pivot = input_array[0]
	less = [x for x in input_array[1:] if x <= pivot]
	great = [x for x in input_array[1:] if x > pivot]
	return quick_sort(less) + [pivot] + quick_sort(great)


if __name__ == '__main__':
	input_array = np.random.randint(1, 100, 5)
	print(input_array)
	print(quick_sort(input_array))
