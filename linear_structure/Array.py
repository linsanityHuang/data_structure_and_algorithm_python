class Array(object):
	
	def __init__(self, size=32, init=None):
		self._size = size
		self._items = [init] * size
		
	def __getitem__(self, index):
		if not isinstance(index, int):
			raise IndexError('index must be int')
		elif index >= self._size:
			raise IndexError('out of index, the maxsize is %s' % self._size)
		return self._items[index]
	
	def __setitem__(self, index, value):
		self._items[index] = value
		
	def __len__(self):
		return self._size
	
	def clear(self, value=None):
		for i in range(len(self._items)):
			self._items[i] = value
			
	def __iter__(self):
		for item in self._items:
			yield item

			
if __name__ == '__main__':
	array = Array()
	for i in range(43):
		array[i] = 2*i
		
	print(array[43])

