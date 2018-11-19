# coding=utf-8
'''
使用数组实现哈希表

哈希函数	abs(hash(key)) % len(self._table)
重哈希的扩容策略 newsize = len(self._table) * 2
'''

from linear_structure.Array import Array


class Slot(object):

	def __init__(self, key, value):
		self.key, self.value = key, value


class HashTable(object):
	UNUSED = None  # slot没被使用过
	EMPTY = Slot(None, None)  # 使用过被删除
	
	def __init__(self):
		self._table = Array(8, init=HashTable.UNUSED)
		self.length = 0
	
	# 负载因子
	@property
	def _load_factory(self):
		return self.length / float(len(self._table))
	
	def __len__(self):
		return self.length
	
	# 计算key的hash值
	# 例如 abs(hash('a')) % 5 等于2
	def _hash(self, key):
		return abs(hash(key)) % len(self._table)
	
	# 根据key值寻找slot
	# 还以key为'a'为例进行说明
	# 把a传递进去之后计算出来的index是2
	# 这个时候会去验证数组_table的索引2的元素
	def _find_key(self, key):
		index = self._hash(key)
		_len = len(self._table)
		while self._table[index] is not HashTable.UNUSED:
			if self._table[index] is HashTable.EMPTY:
				index = (index * 5 + 1) % _len  # cpython使用的解决哈希冲突的方式
				continue
			elif self._table[index].key == key:
				return index
			else:
				index = (index * 5 + 1) % _len
		return None
	
	def _slot_can_insert(self, index):
		return (self._table[index] is HashTable.EMPTY or
				self._table[index] is HashTable.UNUSED)
	
	def _find_slot_for_insert(self, key):
		index = self._hash(key)
		_len = len(self._table)
		while not self._slot_can_insert(index):
			index = (index * 5 + 1) % _len
		return index
	
	def __contains__(self, key):  # in operator
		index = self._find_key(key)
		return index is not None
	
	def _rehash(self):
		old_table = self._table
		newsize = len(self._table) * 2
		self._table = Array(newsize, HashTable.UNUSED)
		self.length = 0
		
		for slot in old_table:
			if slot is not HashTable.UNUSED and slot is not HashTable.EMPTY:
				index = self._find_slot_for_insert(slot.key)
				self._table[index] = slot
				self.length += 1
	
	def add(self, key, value):
		if key in self:  # 更新
			index = self._find_key(key)
			self._table[index].value = value
			return False
		else:
			index = self._find_slot_for_insert(key)
			self._table[index] = Slot(key, value)
			self.length += 1
			if self._load_factory >= 0.8:
				self._rehash()
			return True
	
	def get(self, key, default=None):
		index = self._find_key(key)
		if index is None:
			return default
		else:
			return self._table[index].value
	
	def remove(self, key):
		index = self._find_key(key)
		if index is None:
			raise KeyError()
		value = self._table[index].value
		self.length -= 1
		self._table[index] = HashTable.EMPTY
		return value
	
	def __iter__(self):
		for slot in self._table:
			if slot not in (HashTable.EMPTY, HashTable.UNUSED):
				yield slot.key


if __name__ == '__main__':
	h = HashTable()
	h.add('a', 0)
	h.add('b', 1)
	h.add('c', 2)
	
	assert len(h) == 3
	assert h.get('a') == 0
	assert h.get('b') == 1
	assert h.get('ssdgfj') is None
	
	h.remove('a')
	assert h.get('a') is None
	assert sorted(list(h)) == ['b', 'c']
	
	n = 50
	for i in range(n):
		h.add(i, i)
	for i in range(n):
		assert h.get(i) == i
