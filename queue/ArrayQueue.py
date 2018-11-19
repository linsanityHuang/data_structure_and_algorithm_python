from linear_structure.Array import Array


class ArrayQueue(object):
	'''
	使用数组实现队列
	'''
	def __init__(self, maxsize):
		self.maxsize = maxsize
		self.array = Array(maxsize)
		# head在push操作的时候加1，因此这个值会push的进行而一直增加，
		# 但是根据head对maxsize取余得到的index会一直在0到maxsize-1之间，保证value能够存储在数组中
		self.head = 0
		# 同理，tail会在pop操作的时候加1，保证下次要pop出去的value的位置
		self.tail = 0
		# 在队列的push和pop的操作过程中，没有value被删除，只是原有的元素被覆盖了。
	
	def __len__(self):
		return self.head - self.tail
	
	def push(self, value):
		'''
		用数组实现的queue在push操作的时候，除了把value插入到指定位置之外，还把head标记往前移动了一个位置
		当head的值大于等于self.maxsize的时候，如果还能够插入，说明此时队列未满，也说明已经pop了一些元素，导致tail的值往前移动了
		那么，再push的话就会覆盖之前被pop掉的元素。
		:param value:
		:return:
		'''
		if len(self) >= self.maxsize:
			raise Exception('queue full')
		self.array[self.head % self.maxsize] = value
		self.head += 1
	
	def pop(self):
		'''
		用数组实现的queue在pop的时候并没有把元素从队列中清除
		仅仅是把tail标记往前移动了一个位置
		:return:
		'''
		value = self.array[self.tail % self.maxsize]
		self.tail += 1
		return value
	
	def __repr__(self):
		return '<ArrayQueue: [%s]>' % ', '.join([str(item) for item in self.array if item is not None])
	
	
if __name__ == '__main__':
	size = 5
	q = ArrayQueue(size)
	q.push(15)
	q.push(0)
	q.push(-1)
	print(q)
	assert q.pop() == 15
	q.push(6)
	q.push(1)
	q.push(3)
	assert q.pop() == 0
	assert q.pop() == -1
	print(q)
