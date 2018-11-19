import numpy as np


def insert_sort(input_array):
	n = len(input_array)
	if n <= 1:
		return input_array
	
	for i in range(n):
		for j in range(i, 0, -1):
			if input_array[j] < input_array[j-1]:
				input_array[j-1], input_array[j] = input_array[j], input_array[j-1]
			else:
				break
	return input_array


if __name__ == '__main__':
	input_array = np.random.randint(1, 100, 5)
	print(input_array)
	print(insert_sort(input_array))
