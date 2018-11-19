from hash_table.hashtable import HashTable
'''
继承HashTable实现字典
'''


class DictADT(HashTable):
	
	def __setitem__(self, key, value):
		self.add(key, value)
	
	def __getitem__(self, key):
		if key not in self:
			raise KeyError()
		else:
			return self.get(key)
	
	def _iter_slot(self):
		for slot in self._table:
			if slot not in (HashTable.EMPTY, HashTable.UNUSED):
				yield slot
	
	def items(self):
		for slot in self._iter_slot():
			yield (slot.key, slot.value)
	
	def keys(self):
		for slot in self._iter_slot():
			yield slot.key
	
	def values(self):
		for slot in self._iter_slot():
			yield slot.value


if __name__ == '__main__':
	import random
	d = DictADT()
	
	d['a'] = 1
	for key, value in d.items():
		print(key, value)
	
	assert d['a'] == 1
	d.remove('a')
	
	l = list(range(30))
	random.shuffle(l)
	for i in l:
		d[i] = i
	
	for i in range(30):
		assert d[i] == i
	
	assert sorted(list(d.keys())) == sorted(l)

