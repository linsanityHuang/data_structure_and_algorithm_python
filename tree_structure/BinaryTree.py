# coding=utf-8
'''
树又分为三种遍历方式:

先(根)序遍历: 先处理根，之后是左子树，然后是右子树
中(根)序遍历: 先处理左子树，之后是根，最后是右子树
后(根)序遍历: 先处理左子树，之后是右子树，最后是根
'''


class BinTreeNode(object):
	'''
	二叉树节点
	'''
	def __init__(self, data, left=None, right=None):
		self.data, self.left, self.right = data, left, right
	
	def __repr__(self):
		left = self.left.data if self.left is not None else None
		right = self.right.data if self.right is not None else None
		return '<BinTreeNode: %s, left: %s, right: %s>' % (self.data, left, right)


class BinTree(object):
	def __init__(self, root=None):
		self.root = root
	
	@classmethod
	def build_from(cls, node_list):
		'''
		通过节点信息构建二叉树
		第一次遍历构造node节点
		第二次遍历给root和子节点赋值
		最后用root初始化这个类并返回一个对象
		:param node_list:
			[
				{'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
				{'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
			]
		:return:
		'''
		node_dict = {}
		for node_data in node_list:
			data = node_data['data']
			node_dict[data] = BinTreeNode(data)
		for node_data in node_list:
			data = node_data['data']
			node = node_dict[data]
			if node_data['is_root']:
				root = node
			node.left = node_dict.get(node_data['left'])
			node.right = node_dict.get(node_data['right'])
		for key, value in node_dict.items():
			print(key, value)
		return cls(root)

	def preorder_trav(self, subtree):
		'''
		先（根）序遍历
		'''
		if subtree is not None:
			print(subtree.data)  # 递归函数里先处理根
			self.preorder_trav(subtree.left)  # 递归处理左子树
			self.preorder_trav(subtree.right)  # 递归处理右子树
			
	def postorder_trav(self, subtree):
		'''
		后（根）序遍历
		'''
		if subtree is not None:
			self.preorder_trav(subtree.left)  # 递归处理左子树
			self.preorder_trav(subtree.right)  # 递归处理右子树
			print(subtree.data)  # 递归函数里先处理根
			
	def midorder_trav(self, subtree):
		'''
		中序遍历
		:param subtree:
		:return:
		'''
		if subtree is not None:
			self.midorder_trav(subtree.left)
			print(subtree.data)
			self.midorder_trav(subtree.right)
			
	# 反转二叉树
	def reverse(self, subtree):
		if subtree is not None:
			subtree.left, subtree.right = subtree.right, subtree.left
			self.reverse(subtree.left)
			self.reverse(subtree.right)


if __name__ == '__main__':
	node_list = [
		{'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
		{'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
		{'data': 'D', 'left': None, 'right': None, 'is_root': False},
		{'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
		{'data': 'H', 'left': None, 'right': None, 'is_root': False},
		{'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
		{'data': 'F', 'left': None, 'right': None, 'is_root': False},
		{'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
		{'data': 'I', 'left': None, 'right': None, 'is_root': False},
		{'data': 'J', 'left': None, 'right': None, 'is_root': False},
	]
	
	btree = BinTree.build_from(node_list)
	btree.preorder_trav(btree.root)
	# btree.midorder_trav(btree.root)
	# btree.postorder_trav(btree.root)
	btree.reverse(btree.root)
	print('二叉树反转后')
	btree.preorder_trav(btree.root)
