from heap.max_heap import MaxHeap
from heap.min_heap import MinHeap
import numpy as np
'''
堆排序
使用最大堆排序的话，得到的是倒序排列的顺序，因为最大堆的根节点存储的是最大值
'''


def max_heap_sort(array):
	length = len(array)
	maxheap = MaxHeap(length)
	for i in array:
		maxheap.add(i)
	res = []
	for i in range(length):
		res.append(maxheap.extract())
	return res


def min_heap_sort(array):
	length = len(array)
	maxheap = MinHeap(length)
	for i in array:
		maxheap.add(i)
	res = []
	for i in range(length):
		res.append(maxheap.extract())
	return res


if __name__ == '__main__':
	np.random.seed(1)
	print('最大堆排序')
	input_list = list(np.random.randint(1, 100, 10))
	print('排序前:', input_list)
	min_heap_sorted_list = min_heap_sort(input_list)
	max_heap_sorted_list = max_heap_sort(input_list)
	print('最小堆排序:', min_heap_sorted_list)
	print('最大堆排序:', max_heap_sorted_list)

