# coding=utf-8
from linear_structure.Array import Array
import numpy as np
'''
##
堆是一种完全二叉树，有最大堆和最小堆两种。

最大堆: 对于每个非叶子节点 V，V 的值都比它的两个孩子大，称为 最大堆特性(heap order property) 最大堆里的根总是存储最大值，最小的值存储在叶节点。
最小堆：和最大堆相反，每个非叶子节点 V，V 的两个孩子的值都比它大。

##
堆提供了很有限的几个操作：

插入新的值：插入比较麻烦的就是需要维持堆的特性。需要 sift-up 操作，具体会在视频和代码里解释，文字描述起来比较麻烦。

获取并移除根节点的值：每次我们都可以获取最大值或者最小值。这个时候需要把底层最右边的节点值替换到 root 节点之后 执行 sift-down 操作。

##
用数组就能实现堆

因为完全二叉树的特性，树不会有间隙。对于数组里的一个下标 i，我们可以得到它的父亲和孩子的节点对应的下标：
也就是对于每一个元素，如果其下标是i，那么可以得到其父节点和两个子节点

parent = int((i-1) / 2)    # 取整

left = 2 * i + 1
right = 2 * i + 2
超出下标表示没有对应的孩子节点。
'''


class MaxHeap(object):
	def __init__(self, maxsize=None):
		# 最大堆最多存储元素的个数
		self.maxsize = maxsize
		# 最大堆存储元素的数据结构array
		self._elements = Array(maxsize)
		# 堆当前存储的元素个数
		self._count = 0

	def __len__(self):
		return self._count
	
	def __repr__(self):
		return '<MaxHeap: [%s]>' % ', '.join([str(x) for x in self._elements])

	def add(self, value):
		'''
		添加一个值到最大堆中
		首先加载数组的末尾
		然后再维持堆的特性：
		添加在数组末尾的元素与父元素进行比较，只要其大于父元素的值，就与父元素进行交换
		这个交换过程需要递归进行，递归出口，就是父元素的下标小于等于0，
		此时，被添加的元素已经成为root节点，也就不需要再进行比较了。
		:param value: 要添加的值
		:return:
		'''
		if self._count >= self.maxsize:
			raise Exception('full')
		self._elements[self._count] = value
		# 维持堆的特性，从最后一个元素开始，传入的是最后一个元素的下标
		self._siftup(self._count)
		self._count += 1

	def _siftup(self, ndx):
		'''
		递归交换直到满足最大堆特性
		:param ndx:
		:return:
		'''
		if ndx > 0:
			parent = int((ndx-1)/2)
			# 如果插入的值大于 parent，一直交换
			if self._elements[ndx] > self._elements[parent]:
				self._elements[ndx], self._elements[parent] = self._elements[parent], self._elements[ndx]
				# 递归
				self._siftup(parent)

	def extract(self):
		'''
		获取并移除根节点
		每次移除的都死堆中的最大值
		移除最大值之后，把数组中最后一个元素放到根节点的位置上
		与其左右两个子节点进行比较（如果左右两个子节点都存在的话，如果右子节点存在的话，左子节点必然存在）
		与两个子节点中
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
		# 默认传入的下标就是最大的元素
		larger = ndx
		# 只有两种情况下才会发生交换
		# 1、左子节点存在，左子节点大于等于父节点且大于等于右子节点
		if left < self._count \
			and self._elements[left] >= self._elements[larger] \
			and self._elements[left] >= self._elements[right]:
			larger = left
		# 2、右子节点存在，右子节点大于等于父节点且大于等于左子节点
		elif right < self._count \
				and self._elements[right] >= self._elements[larger]\
				and self._elements[right] >= self._elements[left]:
			larger = right
		if larger != ndx:
			self._elements[larger], self._elements[ndx] = self._elements[ndx], self._elements[larger]
			self._siftdown(larger)


if __name__ == '__main__':
	n = 10
	h = MaxHeap(n)
	# np.random.seed(1)
	for i in np.random.randint(1, 100, n):
		h.add(i)
		print(h)
	
	for _ in range(n):
		print(h.extract())
