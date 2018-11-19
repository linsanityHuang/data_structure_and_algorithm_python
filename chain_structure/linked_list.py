'''
单链表
'''


class Node(object):
	"""
	表示链表中的每一个元素
	节点包括value属性和下一个节点的引用
	"""
	def __init__(self, value=None, next=None):
		self.value, self.next = value, next
		
	def __repr__(self):
		return '<Node: value: {}, next={}>'.format(self.value, self.next)
	

class LinkedList(object):
	"""
	单链表
	-> [root] -> [node0] -> [node1] -> [node2] -> None
	"""
	def __init__(self, maxsize=None):
		self.maxsize = maxsize
		self.root = Node()
		self.tailnode = None
		self.length = 0

	def __len__(self):
		return self.length
	
	# 单链表在尾节点的后面追加，首先要获取尾节点
	# 如果尾节点是None的话，说明链表为空, 表明此时仅有一个root节点
	# 此时，只需要把要追加的节点追加在根节点后面
	# 如果尾节点不是None的话，就把尾节点的next指向要追加的节点
	# 最后更新尾节点
	# O(1)
	def append(self, value):
		if self.maxsize is not None and len(self) >= self.maxsize:
			raise Exception("LinkedList is Full")
		# 构造节点
		node = Node(value)
		tailnode = self.tailnode
		# 还没有append过，length=0，追加到root后
		if tailnode is None:
			self.root.next = node
		# 否则追加到最后一个节点的后边，并且更新最后一个节点是刚append的节点
		else:
			tailnode.next = node
		self.tailnode = node
		self.length += 1
	
	# 单链表在头节点的后面追加，首先要获取头节点
	# 头结点就是根节点的下一个节点
	def appendleft(self, value):
		if self.maxsize is not None and len(self) >= self.maxsize:
			raise Exception('LinkedList is Full')
		node = Node(value)
		# 如果原链表为空，插入第一个元素需要设置tailnode
		if self.tailnode is None:
			self.tailnode = node
		
		headnode = self.root.next
		self.root.next = node
		node.next = headnode
		self.length += 1

	# 遍历单链表，从链表的头结点到尾节点
	# 首先获取链表的头结点作为当前节点，
	# 如果当前节点不是尾节点，就yield出当前节点，并把当前节点更新为当前节点的下一个节点
	# 循环结束后，yield出被更新但是没有yield的当前节点
	def iter_node(self):
		curnode = self.root.next
		# 从第一个节点开始遍历
		while curnode is not self.tailnode and curnode is not None:
			yield curnode
			# 移动到下一个节点
			curnode = curnode.next
		if curnode is not None:
			yield curnode

	def __iter__(self):
		for node in self.iter_node():
			if node is not None:
				yield node.value

	# 删除包含值的一个节点，将其前一个节点的next指向被删除节点的下一个即可
	# O(n)
	def remove(self, value):
		prevnode = self.root
		for curnode in self.iter_node():
			if curnode.value == value:
				prevnode.next = curnode.next
				if curnode is self.tailnode:
					self.tailnode = prevnode
				del curnode
				self.length -= 1
				return 1
			else:
				prevnode = curnode
		return -1

	# 查找一个节点，返回序号，从0开始
	# O(n)
	def find(self, value):
		index = 0
		for node in self.iter_node():
			if node.value == value:
				return index
			index += 1
		return -1
	
	# 删除尾节点
	def pop(self):
		# todo
		if self.root.next is None:
			raise Exception('pop from empty LinkedList')
		prevnode = self.root
		for curnode in self.iter_node():
			if curnode is self.tailnode and curnode is not self.root:
				value = curnode.value
				# 删除当前尾节点
				del curnode
				prevnode.next = None
				self.tailnode = prevnode
				self.length -= 1
				return value
			else:
				prevnode = curnode
	
	# 删除单链表的头节点
	# 单链表的头结点就是根节点的下一个节点
	# 首先获取头结点，判断是否为None
	# 如果为None，说明链表为空，则需要抛出异常
	# 如果不为None，则需要把头结点的下一个节点赋值给根节点的下一个节点，并且把单链表的长度减一
	# 然后删除头结点，并返回其value
	# O(1)
	def popleft(self):
		if self.root.next is None:
			raise Exception('pop from empty LinkedList')
		headnode = self.root.next
		self.root.next = headnode.next
		self.length -= 1
		value = headnode.value
		
		# 如果删除的是尾节点，需要把尾节点置为None
		if self.tailnode is headnode:
			self.tailnode = None
		del headnode
		return value
	
	# 把new_value插入到value之前
	# 首先需要找到value所在的节点，然后获取该节点的前一个节点
	# 然后把要插入的节点追加在该节点的后面
	# 最后把要插入节点的下一个节点赋值执行该节点
	def insert(self, value, new_value):
		new_node = Node(new_value)
		prevnode = self.root
		for node in self.iter_node():
			if node.value == value:
				prevnode.next = new_node
				new_node.next = node
				self.length += 1
			else:
				prevnode = node
	
	# 清空单链表
	def clear(self):
		for node in self.iter_node():
			del node
		self.root.next = None
		self.length = 0
		self.tailnode = None
		
	def is_full(self):
		# 如果链表的大小不限制，返回false
		if self.maxsize is None:
			return False
		elif len(self) < self.maxsize:
			return False
		else:
			return True
	
	def is_empty(self):
		return len(self) == 0


if __name__ == '__main__':
	ll = LinkedList()
	
	for i in range(4):
		ll.append(i)
	
	assert list(ll) == [0, 1, 2, 3]
	
	assert ll.pop() == 3
	assert ll.pop() == 2
	assert ll.pop() == 1
	assert ll.pop() == 0
	assert list(ll) == []
	
	ll.appendleft(0)
	ll.appendleft(-1)
	ll.appendleft(-2)
	assert list(ll) == [-2, -1, 0]
	
	assert ll.find(0) == 2
	assert ll.find(-2) == 0
	
	assert len(ll) == 3
	assert ll.remove(-2) == 1
	
	assert list(ll) == [-1, 0]
	print(ll.pop())
	# assert ll.pop() == 0
	# assert ll.pop() == -1
