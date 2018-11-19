from typing import Optional


class Node:
	def __init__(self, value: int, next_=None):
		self.value, self.next = value, next_


class LinkedList:
	
	def __init__(self, max_size=None):
		self.max_size = max_size
		self.root = Node()
		self.tail = None
		self.length = 0
	
	def __len__(self):
		return self.length
	
	def append(self, value):
		if self.max_size is not None and len(self) >= self.max_size:
			raise Exception('full')
		
		node = Node(value)
		
		tail_node = self.tail
		if tail_node is None:
			self.root.next = node
		else:
			tail_node.next = node
		self.tail = node
		self.length += 1
		
	def appendleft(self, value):
		if self.max_size is not None and len(self) >= self.max_size:
			raise Exception('full')
		head_node = self.root.next
		node = Node(value)
		self.root.next = node
		node.next = head_node
		self.length += 1
		
	def iter_node(self):
		current_node = self.root.next
		while current_node is not self.tail:
			yield current_node
			current_node = current_node.next
		yield current_node
		
	def __iter__(self):
		for node in self.iter_node():
			yield node.value

	def has_cycle(self) -> bool:
		'''
		检测环
		:return:
		'''
		slow, fast = self.root.next, self.root.next
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
			if slow == fast:
				return True
		return False
	
	def merge_sorted_list(self, other) -> Optional[Node]:
		# head1 =
		pass
