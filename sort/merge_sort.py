import numpy as np
'''
归并排序思想

分解：将待排序的 n 个元素分成各包含 n/2 个元素的子序列
解决：使用归并排序递归排序两个子序列
合并：合并两个已经排序的子序列以产生已排序的答案
'''


def merge_sort(seq):
	if len(seq) <= 1:
		return seq
	else:
		mid = int(len(seq) / 2)
		left = merge_sort(seq[:mid])
		print('left', left)
		right = merge_sort(seq[mid:])
		print('right', right)
		
		# 合并两个有序数组
		new_seq = merge_sorted_list(left, right)
		return new_seq


def merge_sorted_list(sorted_a, sorted_b):
	'''
	合并两个有序数组
	比较两个元素，较小的元素就追加到新数组中，同时移动相应的数组指针，即加一
	'''
	length_a, length_b = len(sorted_a), len(sorted_b)
	a, b = 0, 0
	new_sorted_seq = list()

	while a < length_a and b < length_b:
		if sorted_a[a] < sorted_b[b]:
			new_sorted_seq.append(sorted_a[a])
			a += 1
		else:
			new_sorted_seq.append(sorted_b[b])
			b += 1
	
	# 把多余的都放到有序数组里
	while a < length_a:
		new_sorted_seq.append(sorted_a[a])
		a += 1

	while b < length_b:
		new_sorted_seq.append(sorted_b[b])
		b += 1

	return new_sorted_seq


if __name__ == '__main__':
	np.random.seed(2)
	input_list = list(np.random.randint(1, 100, 5))
	print('排序前:', input_list)
	sorted_list = merge_sort(input_list)
	print('排序后:', sorted_list)
