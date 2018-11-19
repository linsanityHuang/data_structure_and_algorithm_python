'''
使用辗转相除法求两个数的最大公约数
'''


def max_common_divisor(a, b):
	print('%s %% %s == %s' % (a, b, a % b))
	while b > 0 and a % b != 0:
		a, b = b, a % b
		print('%s %% %s == %s' % (a, b, a % b))
	return b


if __name__ == '__main__':
	'''
	1112, 695
	'''
	print(max_common_divisor(1112, 695))
