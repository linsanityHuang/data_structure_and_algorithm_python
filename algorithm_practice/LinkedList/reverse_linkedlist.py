from chain_structure.linked_list import LinkedList
import numpy as np
'''
输入一个链表，返回一个反序的链表

通常，这种情况下，我们不希望修改原链表的结构。返回一个反序的链表，这就是经典的“后进先出”，我们可以使用栈实现这种顺序。

每经过一个结点的时候，把该结点放到一个栈中。当遍历完整个链表后，再从栈顶开始逐个输出结点的值，给一个新的链表结构，这样链表就实现了反转。

对于python来讲，不用如此麻烦，我们可以直接使用列表的插入方法，每次插入数据，只插入在首位。
'''


class Solution:
	
	def print_list_from_tail_to_head(self, linkedlist):
		result = []
		while not linkedlist.is_empty():
			result.insert(0, linkedlist.popleft())
		return result


if __name__ == '__main__':
	np.random.seed(1)
	n = 5
	linkedlist = LinkedList(maxsize=n)
	for i in np.random.randint(1, 100, 5):
		# print(i)
		linkedlist.append(i)
	print(list(linkedlist))
	solution = Solution()
	reversed_linkedlist = solution.print_list_from_tail_to_head(linkedlist)
	print(reversed_linkedlist)
