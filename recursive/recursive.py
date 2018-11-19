from collections import deque


def fact(n):
	'''使用递归求n的阶乘'''
	if n == 0:
		return 1
	else:
		return n * fact(n - 1)


def print_num_revursive(n):
	'''使用递归正序打印1-n的数列'''
	if n > 0:
		print_num_revursive(n - 1)
		print(n)
		

def print_num_revursive_reverse(n):
	'''使用递归倒序打印1-n的数列'''
	if n > 0:
		print_num_revursive_reverse(n - 1)
		print(n)


class Stack(object):
	'''使用collections中的双端队列实现栈'''
	def __init__(self):
		self._deque = deque()
		
	def push(self, value):
		return self._deque.append(value)
	
	def pop(self):
		return self._deque.pop()
	
	def is_empty(self):
		return len(self._deque) == 0


def print_num_use_stack(n):
	'''
	使用自己实现的栈，模拟计算机执行递归打印数字
	:param n:
	:return:
	'''
	s = Stack()
	while n > 0:
		s.push(n)
		n -= 1
	
	while not s.is_empty():
		print(s.pop())


# print_num_use_stack(10)

