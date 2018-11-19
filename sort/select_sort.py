import numpy as np


def select_sort(input_list):
	'''
	选择排序
	首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
	然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
	以此类推，直到所有元素均排序完毕。
	'''
	n = len(input_list)
	if n <= 1:
		return input_list

	for i in range(n):
		min = i
		for j in range(i + 1, n):
			if input_list[j] < input_list[min]:
				min = j
		if min != i:
			input_list[i], input_list[min] = input_list[min], input_list[i]
		print('排序中:', input_list)
	return input_list


if __name__ == '__main__':
	input_list = list(np.random.randint(1, 100, 5))
	print('排序前:', input_list)
	sorted_list = select_sort(input_list)
	print('排序后:', sorted_list)
