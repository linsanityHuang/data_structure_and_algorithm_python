import numpy as np


def binary_search(input_array, target):
	n = len(input_array)
	if n == 0:
		return -1
	low = 0
	high = n-1
	while low <= high:
		mid = (low + high) // 2
		if input_array[mid] == target:
			return mid
		elif input_array[mid] > target:
			high = mid - 1
		elif input_array[mid] < target:
			low = mid + 1
	return -1


if __name__ == '__main__':
	input_array = [34, 49, 74, 91, 95]
	print(input_array)
	target = int(input('target: '))
	print(binary_search(input_array, target))
