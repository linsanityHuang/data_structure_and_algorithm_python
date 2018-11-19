
class ArrayStack:
	'''
	基于数组的顺序栈
	'''
	def __init__(self, size):
		self.items = [None for i in range(size)]
		self.size = size
		self.count = 0
		
	def push(self, item):
		'''
		入栈
		:param item:
		:return:
		'''
		if self.count == self.size:
			return False
		self.items[self.count] = item
		self.count += 1
		return True
	
	def pop(self):
		'''
		出栈
		:return:
		'''
		if self.count == 0:
			return None
		self.count -= 1
		return self.items[self.count]
	
	def top(self):
		'''
		返回栈顶元素
		:return:
		'''
		return self.items[self.count-1]


if __name__ == '__main__':
	stack = ArrayStack(3)
	print(stack.top())
	stack.push(0)
	stack.push(1)
	stack.push(10)
	stack.push(3)
	print(stack.top())
	print(stack.items)
	stack.push(3)
	print(stack.items)
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
