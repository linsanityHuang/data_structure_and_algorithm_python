import numpy as np
'''
二叉查找树是这样一种二叉树结构，它的每个节点包含一个 key 和它附带的数据，对于每个内部节点 V：

1、所有 key 小于 V 的都被存储在 V 的左子树
2、所有 key 大于 V 的都存储在 V 的右子树

注意这个限制条件，可别和堆搞混了。

说白了就是对于每个内部节点，左子树的 key 都比它小，右子树都比它大。

如果中序遍历(二叉树遍历讲过了)这颗二叉树，你会发现输出的顺序正好是有序的。
'''


class BSTNode:
	def __init__(self, key, value, left=None, right=None):
		'''
		
		:param key: key用来确定该节点在树中的位置
		:param value: value是这个节点所保存的数据
		:param left: left指向该节点的左子节点
		:param right: right指向该节点的右子节点
		'''
		self.key, self.value, self.left, self.right = key, value, left, right

	def __repr__(self):
		left = None if self.left is None else self.left.key
		right = None if self.right is None else self.right.key
		return '<BSTNode: key: %s, value: %s, left: %s, right: %s>' % (self.key, self.value, left, right)


class BSTree:
	def __init__(self, root=None, size=0):
		self.root = root
		self.size = size
		
	@classmethod
	def build_from(cls, node_list):
		cls.size = 0
		key_to_node_dict = {}
		for node_dict in node_list:
			key = node_dict['key']
			# 构建二叉查找树的时候，每个节点的key和value一致
			key_to_node_dict[key] = BSTNode(key, value=key)
			
		for node_dict in node_list:
			key = node_dict['key']
			node = key_to_node_dict[key]
			if node_dict['is_root']:
				root = node
			node.left = key_to_node_dict.get(node_dict['left'])
			node.right = key_to_node_dict.get(node_dict['right'])
			cls.size += 1
		# for key, value in key_to_node_dict.items():
		# 	print(key, value)
		return cls(root)
	
	def _bst_search(self, subtree, key):
		'''
		根据key寻找对应节点
		:param subtree:
		:param key:
		:return:
		'''
		if subtree is None:
			return None
		elif key < subtree.key:
			return self._bst_search(subtree.left, key)
		elif key > subtree.key:
			return self._bst_search(subtree.right, key)
		else:
			return subtree
		
	def get(self, key, default=None):
		node = self._bst_search(self.root, key)
		if node is None:
			return default
		else:
			return node.value
		
	def __contains__(self, key):
		return self._bst_search(self.root, key) is not None
	
	def _bst_min_node(self, subtree):
		'''
		寻找二叉查找树的最小节点
		由于二叉查找树的特性，其最小节点肯定位于左子树
		所以，只要递归左子树就可以找到
		:param subtree:
		:return:
		'''
		if subtree is None:
			return None
		elif subtree.left is None:
			return subtree
		else:
			return self._bst_min_node(subtree.left)
		
	def bst_min(self):
		node = self._bst_min_node(self.root)
		return node.value if node else None
	
	def _bst_insert(self, subtree, key, value):
		'''
		插入并且返回根节点
		:param subtree:
		:param key:
		:param value:
		:return:
		'''
		# 插入的节点一定是根节点，包括 root 为空的情况
		if subtree is None:
			subtree = BSTNode(key, value)
		elif key < subtree.key:
			subtree.left = self._bst_insert(subtree.left, key, value)
		elif key > subtree.key:
			subtree.right = self._bst_insert(subtree.right, key, value)
		return subtree
	
	def add(self, key, value):
		'''
		往二叉查找树中插入节点
		如果key已经在树中，就更新key对应节点的value
		如果key不在树中，先寻找要插入的节点，然后插入
		:param key:
		:param value:
		:return:
		'''
		node = self._bst_search(self.root, key)
		if node is not None:
			node.value = value
			return False
		else:
			self.root = self._bst_insert(self.root, key, value)
			self.size += 1
			return True
	
	def _bst_remove(self, subtree, key):
		"""删除节点并返回根节点"""
		if subtree is None:
			return None
		elif key < subtree.key:
			subtree.left = self._bst_remove(subtree.left, key)
			return subtree
		elif key > subtree.key:
			subtree.right = self._bst_remove(subtree.right, key)
			return subtree
		else:  # 找到了需要删除的节点
			if subtree.left is None and subtree.right is None:  # 叶节点，返回 None 把其父亲指向它的指针置为 None
				return None
			elif subtree.left is None or subtree.right is None:  # 只有一个孩子
				if subtree.left is not None:
					return subtree.left  # 返回它的孩子并让它的父亲指过去
				else:
					return subtree.right
			else:  # 俩孩子，寻找后继节点替换，并从待删节点的右子树中删除后继节点
				successor_node = self._bst_min_node(subtree.right)
				subtree.key, subtree.value = successor_node.key, successor_node.value
				subtree.right = self._bst_remove(subtree.right, successor_node.key)
				return subtree
	
	def remove(self, key):
		assert key in self
		self.size -= 1
		return self._bst_remove(self.root, key)
	
	def mid_order_iter(self, subtree):
		if subtree is not None:
			self.mid_order_iter(subtree.left)
			print(subtree.key)
			self.mid_order_iter(subtree.right)
		
		
if __name__ == '__main__':
	# NODE_LIST = [
	# 	{'key': 60, 'left': 12, 'right': 90, 'is_root': True},
	# 	{'key': 12, 'left': 4, 'right': 41, 'is_root': False},
	# 	{'key': 4, 'left': 1, 'right': None, 'is_root': False},
	# 	{'key': 1, 'left': None, 'right': None, 'is_root': False},
	# 	{'key': 41, 'left': 29, 'right': None, 'is_root': False},
	# 	{'key': 29, 'left': 23, 'right': 37, 'is_root': False},
	# 	{'key': 23, 'left': None, 'right': None, 'is_root': False},
	# 	{'key': 37, 'left': None, 'right': None, 'is_root': False},
	# 	{'key': 90, 'left': 71, 'right': 100, 'is_root': False},
	# 	{'key': 71, 'left': None, 'right': 84, 'is_root': False},
	# 	{'key': 100, 'left': None, 'right': None, 'is_root': False},
	# 	{'key': 84, 'left': None, 'right': None, 'is_root': False},
	# ]
	# bst = BSTree.build_from(NODE_LIST)
	# np.random.seed(11)
	n = 3
	root = BSTNode(50, 50)
	bst = BSTree(root=root)
	for i in np.random.randint(1, 100, n):
		bst.add(i, i)
	print(bst.root)
	bst.mid_order_iter(bst.root)
	# print(bst.bst_min())
	bst.add(0, 0)
	assert bst.bst_min() == 0
	
	bst.add(12, 12)
	bst.remove(12)
	assert bst.get(12) is None
	
	bst.add(1, 1)
	bst.remove(1)
	assert bst.get(1) is None
	
	bst.add(29, 29)
	bst.remove(29)
	assert bst.get(29) is None
