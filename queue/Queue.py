from chain_structure.linked_list import LinkedList
'''
使用单向链表实现普通队列（先进先出FIFO）
'''


class Queue(object):
	
	def __init__(self, maxsize=None):
		self.maxsize = maxsize
		self._item_link_list = LinkedList()
		
	def __len__(self):
		return len(self._item_link_list)
	
	# O(1)
	def push(self, value):
		'''
		队尾添加元素
		'''
		return self._item_link_list.append(value)
	
	def pop(self):
		'''
		队列头部删除元素
		'''
		if len(self) <= 0:
			raise Exception('empty queue')
		return self._item_link_list.popleft()


if __name__ == '__main__':
	q = Queue()
	q.push(0)
	q.push(1)
	q.push(2)
	
	assert len(q) == 3
	
	assert q.pop() == 0
	assert q.pop() == 1
	assert q.pop() == 2
