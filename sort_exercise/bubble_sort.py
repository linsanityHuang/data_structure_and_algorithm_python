import numpy as np


def bubble_sort(input_array):
	n = len(input_array)
	if n <= 1:
		return input_array
	
	for i in range(n-1):
		for j in range(n-1-i):
			if input_array[j] > input_array[j+1]:
				input_array[j], input_array[j+1] = input_array[j+1], input_array[j]
	return input_array


if __name__ == '__main__':
	input_array = np.random.randint(1, 100, 5)
	print(input_array)
	print(bubble_sort(input_array))
	
	
