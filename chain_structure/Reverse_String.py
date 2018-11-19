from chain_structure.linked_list import LinkedList
'''
使用单链表判断是否为回文字符串
'''


def is_reversed_str(word):
	if not isinstance(word, str):
		return
	str_linkedlist = LinkedList(maxsize=len(word))
	for item in word:
		str_linkedlist.append(item)
	
	size = len(str_linkedlist)
	flag = True
	for _ in range(size // 2):
		if str_linkedlist.pop() != str_linkedlist.popleft():
			flag = False
			break
	return flag


if __name__ == '__main__':
	if is_reversed_str('qwe1ewq'):
		print('是')
	else:
		print('不是')
