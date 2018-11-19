import numpy as np


def binary_serach(input_list, target):
	'''
	二分查找法
	输入的数组必须是有序的
	'''
	n = len(input_list)
	input_list = sorted(input_list)
	low = 0
	high = n - 1
	while low <= high:			# 必须是小于等于，不然可能会漏掉一些边界情况
		mid = (low + high) // 2
		if target < input_list[mid]:
			high = mid - 1
		elif target > input_list[mid]:
			low = mid + 1
		else:
			return mid
	return -1


if __name__ == '__main__':
	# input_list = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100]
	np.random.seed(10)
	input_list = list(np.random.randint(1, 1000, 5))
	
	assert len(input_list) == 5
	print(sorted(input_list))
	print(binary_serach(sorted(input_list), 266))
