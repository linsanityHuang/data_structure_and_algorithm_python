'''
演示哈希冲突后，Python内置的解决方法，二次探查法
'''

inserted_index_set = set()
M = 13


def h(key, M=13):
	return key % M


to_insert = [765, 431, 96, 142, 579, 226, 903, 388]

# 对于每一个要存储的数字，都先计算其hash值index，这个index就是这个数字要存储的位置
# 然后判断index是否在集合inserted_index_set中
# 存在，说明发生了hash冲突，重新计算index的值，知道index不在集合中出现，
# 不存在，直接按照index存储该数字
for number in to_insert:
	index = h(number)
	first_index = index
	i = 1
	while index in inserted_index_set:
		print('\th({number}) = {number} % M = {index} collision'.format(number=number, index=index))
		index = (first_index + i * i) % M
		i += 1
	else:
		print('h({number}) = {number} % M = {index}'.format(number=number, index=index))
		inserted_index_set.add(index)
