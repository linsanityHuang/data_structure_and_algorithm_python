from heap.max_heap import MaxHeap
'''
使用最大堆实现优先级队列

优先级队列(Priority Queue) 顾名思义，就是入队的时候可以给一个优先级，通常是个数字或者时间戳等，
当出队的时候我们希望按照给定的优先级出队
'''


class PriorityQueue:
	def __init__(self, maxsize):
		self.maxsize = maxsize
		self._maxheap = MaxHeap(maxsize)
		
	def push(self, priority, value):
		
		# 注意这里把这个 tuple push 进去，python 比较 tuple 从第一个开始比较
		# 这样就很巧妙地实现了按照优先级排序
		# (4, 'c') > (1, 'b') True
		# (4, 'c') > (5, 'b') False
		# 入队的时候会根据 priority 维持堆的特性
		entry = (priority, value)
		self._maxheap.add(entry)
	
	def pop(self, with_priority=False):
		entry = self._maxheap.extract()
		if with_priority:
			return entry
		else:
			return entry[1]
	
	def is_empty(self):
		return len(self._maxheap) == 0


if __name__ == '__main__':
	size = 5
	pq = PriorityQueue(size)
	pq.push(5, 'purple')
	pq.push(0, 'white')
	pq.push(3, 'orange')
	pq.push(1, 'black')
	
	res = []
	while not pq.is_empty():
		res.append(pq.pop(with_priority=True))
	# assert res == ['purple', 'orange', 'black', 'white']
	print(res)

