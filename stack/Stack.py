from queue.Deque import Deque
'''
使用双端对列实现栈（后进先出）
'''


class Stack:
	
	def __init__(self):
		self._deque = Deque()
	
	def push(self, value):
		'''
		入栈
		:param value:
		:return:
		'''
		self._deque.push(value)
		
	def pop(self):
		'''
		出栈
		:return:
		'''
		return self._deque.pop()
	
	
if __name__ == '__main__':
	stack = Stack()
	
	stack.push(32)
	stack.push(19)
	stack.push(18)
	stack.push(17)
	
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
	print(stack.pop())
