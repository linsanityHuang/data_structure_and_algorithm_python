from linear_structure.Array import Array
import numpy as np


class MinHeap:
	
	def __init__(self, maxsize=None):
		self.maxsize = maxsize
		self._elements = Array(maxsize)
		self._count = 0

	def __len__(self):
		return self._count
	
	def __repr__(self):
		return '<MaxHeap: [%s]>' % ', '.join([str(x) for x in self._elements])

	def add(self, value):
		'''
		添加一个值到最小堆中
		:param value:
		:return:
		'''
		if self._count >= self.maxsize:
			raise Exception('full')
		self._elements[self._count] = value
		# 维持堆的特性
		self._siftup(self._count)
		self._count += 1
		
	def _siftup(self, ndx):
		'''
		递归交换直到满足最小堆特性
		:param ndx:
		:return:
		'''
		if ndx > 0:
			parent = int((ndx-1)/2)
			# 如果插入的值大于 parent，一直交换
			if self._elements[ndx] < self._elements[parent]:
				self._elements[ndx], self._elements[parent] = self._elements[parent], self._elements[ndx]
				# 递归
				self._siftup(parent)
				
	def extract(self):
		'''
		获取并移除根节点
		:return:
		'''
		if self._count <= 0:
			raise Exception('empty')
		value = self._elements[0]
		self._count -= 1
		self._elements[0] = self._elements[self._count]
		self._siftdown(0)
		return value

	def _siftdown(self, ndx):
		left = 2 * ndx + 1
		right = 2 * ndx + 2
		smaller = ndx

		if left < self._count and \
			self._elements[left] <= self._elements[smaller] and \
			self._elements[left] <= self._elements[right]:
			smaller = left
		elif right < self._count and \
				self._elements[right] <= self._elements[smaller] and \
				self._elements[right] <= self._elements[left]:
			smaller = right
		if smaller != ndx:
			self._elements[smaller], self._elements[ndx] = self._elements[ndx], self._elements[smaller]
			self._siftdown(smaller)


if __name__ == '__main__':
	n = 10
	h = MinHeap(n)
	# np.random.seed(1)
	for i in np.random.randint(1, 100, n):
		h.add(i)
		print(h)
	
	for _ in range(n):
		print(h.extract())
