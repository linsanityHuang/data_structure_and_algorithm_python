import numpy as np


def bubble_sort_v0(input_list):
	'''
	普通冒泡排序
	:param input_list:
	:return:
	'''
	n = len(input_list)
	# 如果数组长度小于等于1，直接返回数组
	if n <= 1:
		return input_list
	for i in range(n-1):
		for j in range(n-1-i):
			if input_list[j] > input_list[j+1]:
				input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
		print('排序中:', input_list)
	return input_list


def bubble_sort(input_list):
	'''
	冒泡排序
	每一次排序，都是比较相邻两个元素，如果第一个元素大于第二个元素，交换这两个元素，否则不做操作
	一共需要进行len(input_list)次排序

	两种改进方法
	1、如果在某次排序过程中，没有发生元素交换，说明已经是有序的，即可停止排序
	2、在每次排序中，记录发生元素交换的最后位置，下次比较的时候，这个位置之后的元素不用进行比较，已经是有序的了
	'''
	n = len(input_list)		# 获取输入list的长度
	if n <= 1:
		return input_list	# 如果list的长度<=1，直接返回
	k = n 					# 记录每次排序过程中，发生交换的最后位置
	for i in range(n-1):
		flag = 1			# 发生交换是修改为0
		for j in range(1, k):	# 优化之前k是n-i
			if input_list[j - 1] > input_list[j]:
				input_list[j - 1], input_list[j] = input_list[j], input_list[j - 1]
				k = j
				flag = 0
		print('排序中:', input_list)
		if flag:			# 如果此次排序没有发生元素交换，则跳出外层循环，排序结束
			break
	return input_list


if __name__ == '__main__':
	# np.random.seed(10)
	print('普通冒泡排序')
	input_list = list(np.random.randint(1, 100, 10))
	print('排序前:', input_list)
	sorted_list = bubble_sort_v0(input_list)
	print('排序后:', sorted_list)
	
	# input_list = list(np.random.randint(1, 100, 10))
	# print('排序前:', input_list)
	# sorted_list = bubble_sort(input_list)
	# print('排序后:', sorted_list)
