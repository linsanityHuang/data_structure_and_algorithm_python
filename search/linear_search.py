# coding=utf-8
'''
线性查找就是从头找到尾，直到符合条件了就返回。

比如在一个 list 中找到一个等于 5 的元素并返回下标：
'''


def linear_search(value, iterable):
	'''
	普通线性查找
	:param value:
	:param iterable:
	:return:
	'''
	for index, val in enumerate(iterable):
		if val == value:
			return index
	return -1


def linear_search_v2(predicate, iterable):
	'''
	传入函数，返回符合函数逻辑的索引列表
	:param predicate:
	:param iterable:
	:return:
	'''
	index_lsit = []
	for index, val in enumerate(iterable):
		if predicate(val):
			index_lsit.append(index)
	return index_lsit


def linear_search_recursive(array, value):
	'''
	通过递归方式实现普通线性查找
	:param array:
	:param value:
	:return:
	'''
	if len(array) == 0:
		return -1
	index = len(array) - 1
	if array[index] == value:
		return index
	return linear_search_recursive(array[0:index], value)


if __name__ == '__main__':
	assert linear_search(5, list(range(8))) == 5
	print(list(range(9)))
	
	assert linear_search_v2(lambda x: x == 5, list(range(10))) == [5]
	assert linear_search_v2(lambda x: x >= 5, list(range(10))) == [5, 6, 7, 8, 9]
	assert linear_search_v2(lambda x: x < 5, list(range(10))) == [0, 1, 2, 3, 4]
	
	assert linear_search_recursive(list(range(9)), 5) == 5
	assert linear_search_recursive(list(range(9)), 8) == 8
	assert linear_search_recursive(list(range(9)), 7) == 7
	assert linear_search_recursive(list(range(9)), 0) == 0
	assert linear_search_recursive(list(range(9)), 10) == -1
