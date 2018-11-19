import numpy as np
'''
快速排序的思想

选择基准值 pivot 将数组分成两个子数组：小于基准值的元素和大于基准值的元素。这个过程称之为 partition

对这两个子数组进行快速排序。

合并结果
'''


def quick_sort(input_list):
	n = len(input_list)
	# # 递归出口，空数组或者只有一个元素的数组都是有序的
	if n <= 1:
		return input_list
	else:
		# 选择第一个元素作为 pivot
		pivot = input_list[0]
		# 构造了两个新列表
		less = [x for x in input_list[1:] if x <= pivot]
		great = [x for x in input_list[1:] if x > pivot]
		return quick_sort(less) + [pivot] + quick_sort(great)


# 上面的快速排序存在两个缺陷
# 1、需要额外的存储空间，我们想实现inplace原地排序
# 2、它的partition操作每次都要两次遍历整个数组

# 优化快速排序
def partition(array, begin, end):
	pivot_index = begin
	pivot = array[pivot_index]
	left = pivot_index + 1
	right = end - 1

	while True:
		while left <= right and array[left] < pivot:
			left += 1

		while right >= left and array[right] >= pivot:
			right -= 1

		if left > right:
			break
		else:
			array[left], array[right] = array[right], array[left]
	array[pivot_index], array[right] = array[right], array[pivot_index]
	return right


def quick_sort_inplace(array, begin, end):		# 左闭右开区间
	'''
	实现 inplace 排序并且改善 partition 操作
	:param array:
	:param begin:
	:param end:
	:return:
	'''
	if begin < end:
		pivot = partition(array, begin, end)
		quick_sort_inplace(array, begin, pivot)
		quick_sort_inplace(array, pivot + 1, end)


if __name__ == '__main__':
	# input_list = [50, 123, 543, 187, 49, 30, 0, 2, 11, 100]
	input_list = list(np.random.randint(1, 1000, 5))
	print('排序前:', input_list)
	sorted_list = quick_sort(input_list)
	print('排序后:', sorted_list)
