from chain_structure.linked_list import LinkedList

'''
基于单链表实现 LRU 缓存淘汰算法
'''


class LRUCache:
	
	def __init__(self, maxsize=None):
		self._cache = LinkedList(maxsize)
		
	def cache(self, value):
		index = self._cache.find(value)
		# 如果value在cache中
		if index != -1:
			self._cache.remove(value)
			self._cache.appendleft(value)
		# 如果value没有在cache中，且cache已满
		elif self._cache.is_full():
			# 删除尾节点
			self._cache.pop()
			# 将新数据插入链表的头部
			self._cache.appendleft(value)
		# 如果value没在cache中，且cache未满
		elif not self._cache.is_full():
			self._cache.appendleft(value)


if __name__ == '__main__':
	cache = LRUCache(5)
	for _ in range(5):
		cache.cache(_)
	print(list(cache._cache))
	cache.cache(5)
	print(list(cache._cache))
	cache.cache(1)
	print(list(cache._cache))
	cache.cache(6)
	print(list(cache._cache))
