from chain_structure.double_link_list import CircualDoubleLinkedList
'''
使用循环双端链表实现双端队列
'''


class Deque:
	
	def __init__(self, maxsize=None):
		self._maxsize = maxsize
		self._double_end_linkedlist = CircualDoubleLinkedList()
	
	# 删除队列尾部元素
	def pop(self):
		if len(self) <= 0:
			raise Exception('pop from empty queue')
		return self._double_end_linkedlist.pop()
	
	# 删除队列头部元素
	def popleft(self):
		if len(self) <= 0:
			raise Exception('pop from empty queue')
		return self._double_end_linkedlist.popleft()
	
	# 添加元素到队列尾部
	def push(self, value):
		if self._maxsize is not None and len(self) >= self._maxsize:
			raise Exception('full')
		self._double_end_linkedlist.append(value)
	
	# 添加元素到队列头部
	def pushleft(self, value):
		if self._maxsize is not None and len(self) >= self._maxsize:
			raise Exception('full')
		self._double_end_linkedlist.appendleft(value)
	
	def __len__(self):
		return len(self._double_end_linkedlist)
	
	def __repr__(self):
		return '<Deque: [%s]>' % ', '.join(str(item) for item in self._double_end_linkedlist)


if __name__ == '__main__':
	deque = Deque(5)
	print(deque)
	deque.pushleft(1)
	deque.pushleft(2)
	deque.pushleft(3)
	print(deque)
	
	# 删除队列尾部的元素
	assert deque.pop() == 1
	print(deque)
	
	# 删除队列头部的元素
	assert deque.popleft() == 3
	print(deque)

	# 在队列尾部添加元素
	deque.push(100)
	deque.push(190)
	deque.push(0)
	print(deque)
	
	# 在队列头部添加元素
	deque.pushleft(-12)
	print(deque)
	print(len(deque))
	# 报错
	deque.pushleft(-12)
