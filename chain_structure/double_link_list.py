# coding=utf-8

# 单链表由于存在删除节点的时间复杂度为O(n)以及只能单向遍历这两个缺陷
# 双链表的节点比单链表的节点多以指向前一个节点的属性


class Node(object):
	"""
	比单链表的节点多了一个指向前一个节点的指针
	"""
	def __init__(self, value=None, prev=None, next=None):
		self.value, self.prev, self.next = value, prev, next


class CircualDoubleLinkedList(object):
	'''
	循环双端链表
	多了个循环，其实就是把root的 prev 指向 tail 节点，串起来
	'''
	def __init__(self, maxsize=None):
		self.maxsize = maxsize
		# 初始化的时候，双端链表的根节点的上一个节点和下一个节点都是根节点自身
		node = Node()
		node.next, node.prev = node, node
		self.root = node
		self.length = 0

	def __len__(self):
		return self.length

	def headnode(self):
		return self.root.next

	def tailnode(self):
		return self.root.prev

	# 在双端链表的末尾添加节点
	# O(1)
	# 一般不用for循环的就是O(1)，有限个步骤
	def append(self, value):
		if self.maxsize is not None and len(self) >= self.maxsize:
			raise Exception('full')
		
		# 构造节点
		node = Node(value=value)
		# 获取尾节点
		tailnode = self.tailnode() or self.root
		
		tailnode.next = node
		node.prev = tailnode
		
		node.next = self.root
		self.root.prev = node

		self.length += 1

	# 在双端链表的头部添加节点
	def appendleft(self, value):
		if self.maxsize is not None and len(self) >= self.maxsize:
			raise Exception('full')
		
		node = Node(value=value)
		
		# 如果双端链表为空
		if self.root.next is self.root:
			node.next = self.root
			node.prev = self.root
			
			self.root.next = node
			self.root.prev = node
		else:
			node.prev = self.root
			headnode = self.root.next
			node.next = headnode
			
			headnode.prev = node
			self.root.next = node
			
		self.length += 1

	# 删除节点, node is not value, O(1)
	# 注意传入的参数是node，而不是value
	def remove(self, node):
		if node is self.root:
			return
		else:
			node.prev.next = node.next
			node.next.prev = node.prev
		self.length -= 1
		return node
	
	# 删除尾节点
	def pop(self):
		if self.root.next is self.root:
			raise Exception('pop from empty circualdoublelinkedlist')
		# 获取尾节点
		tailnode = self.tailnode()
		value = tailnode.value
		self.root.prev = tailnode.prev
		tailnode.prev.next = self.root
		self.length -= 1
		del tailnode
		return value
	
	# 删除头结点
	def popleft(self):
		if self.root.next is self.root:
			raise Exception('pop from empty circualdoublelinkedlist')
		# 获取头结点
		headnode = self.headnode()
		value = headnode.value
		self.root.next = headnode.next
		headnode.next.prev = self.root
		self.length -= 1
		del headnode
		return value
		
	# 遍历双端链表
	def iter_node(self):
		# 如果链表为空直接返回
		if self.root.next is self.root:
			return
		
		# 不为空，则先获取头节点
		curnode = self.root.next
		while curnode.next is not self.root:
			yield curnode
			curnode = curnode.next
		# 上面循环到尾节点结束，但并没有yield尾节点，这里yield尾节点
		yield curnode

	def __iter__(self):
		for node in self.iter_node():
			yield node.value

	# 反向遍历双端链表
	def iter_node_reverse(self):
		if self.root.prev is self.root:
			return
		# 获取尾节点
		curnode = self.root.prev
		while curnode.prev is not self.root:
			yield curnode
			curnode = curnode.prev
		yield curnode
		
	def __reversed__(self):
		for node in self.iter_node_reverse():
			yield node.value


if __name__ == '__main__':
	dll = CircualDoubleLinkedList()
	assert len(dll) == 0

	dll.append(0)
	dll.append(1)
	dll.append(2)

	assert list(dll) == [0, 1, 2]

	assert [value for value in dll] == [0, 1, 2]
	assert [value for value in reversed(dll)] == [2, 1, 0]

	headnode = dll.headnode()
	assert headnode.value == 0
	# O(1)
	dll.remove(headnode)
	assert len(dll) == 2
	assert [value for value in dll] == [1, 2]

	dll.appendleft(0)
	assert [value for value in reversed(dll)] == [2, 1, 0]
	print(list(dll))
	print(dll.pop())
	print(dll.pop())
	print(dll.pop())
	
	assert list(dll) == []
	
	dll.append(0)
	dll.append(1)
	dll.append(2)
	
	print(list(dll))
	print(dll.popleft())
	print(dll.popleft())
	print(dll.popleft())
	assert list(dll) == []
	print(dll.popleft())
