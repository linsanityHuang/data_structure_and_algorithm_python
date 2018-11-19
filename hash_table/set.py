from hash_table.hashtable import HashTable
'''
继承HashTable实现集合set
'''


class SetADT(HashTable):
	
	def add(self, key, value=1):
		return super(SetADT, self).add(key, True)
	
	def __and__(self, other_set):
		'''
		求交集
		:param other_set:
		:return:
		'''
		new_set = SetADT()
		for element_a in self:
			if element_a in other_set:
				new_set.add(element_a)
		return new_set
	
	def __sub__(self, other_set):
		new_set = SetADT()
		for element_a in self:
			if element_a not in other_set:
				new_set.add(element_a)
		return new_set
	
	def __or__(self, other_set):
		new_set = SetADT()
		for element_a in self:
			new_set.add(element_a)
		for element_b in other_set:
			new_set.add(element_b)
		return new_set


if __name__ == '__main__':
	sa = SetADT()
	sa.add(1)
	sa.add(2)
	sa.add(3)
	
	assert 1 in sa
	
	sb = SetADT()
	sb.add(3)
	sb.add(4)
	sb.add(5)
	
	assert sorted(list(sa & sb)) == [3]
	assert sorted(list(sa - sb)) == [1, 2]
	assert sorted(list(sa | sb)) == [1, 2, 3, 4, 5]