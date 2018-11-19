import numpy as np


def insert_sort(input_list):
	'''
	插入排序
	插入排序（英语：Insertion Sort）是一种简单直观的排序算法。
	它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
	插入排序在实现上，通常采用in-place排序（即只需用到O(1)的额外空间的排序），
	因而在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。
	'''
	n = len(input_list)
	if n <= 1:
		return input_list

	for i in range(1, n):
		# print(list(range(1, n)))
		for j in range(i, 0, -1):
			# print(list(range(i, 0, -1)))
			if input_list[j] < input_list[j - 1]:
				input_list[j - 1], input_list[j] = input_list[j], input_list[j - 1]
			else:
				break
		print('排序中:', input_list)
	return input_list


if __name__ == '__main__':
	np.random.seed(2)
	input_list = list(np.random.randint(1, 100, 6))
	print('排序前:', input_list)
	sorted_list = insert_sort(input_list)
	print('排序后:', sorted_list)
