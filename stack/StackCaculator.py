from stack.ArrayStack import ArrayStack


if __name__ == '__main__':
	operator_map = {
		'/': 1,
		'*': 1,
		'+': 0,
		'-': 0,
	}
	arg = '3+5*8-6'
	
	num_stack = ArrayStack(len(arg))
	operator_stack = ArrayStack(len(arg))
	
	for s in arg:
		if s in operator_map.keys():
			top = operator_stack.top()
			while top is not None and operator_map.get(s) <= operator_map.get(top):
				print(top)
				num1 = num_stack.pop()
				num2 = num_stack.pop()
				res = eval('%s%s%s' % (num1, top, num2))
				num_stack.push(res)
				operator_stack.pop()
				top = operator_stack.top()
			else:
				operator_stack.push(s)
		else:
			num_stack.push(s)
			
	print(num_stack.items)
	print(operator_stack.items)
