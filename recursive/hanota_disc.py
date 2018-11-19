'''
借助递归思想，完成汉诺塔圆盘移动问题

假设我们已经知道了如何移动上边的四个盘子到 B(pole2)，现在把最大的盘子从 A -> C 就很简单了。

当把最大的盘子移动到 C 之后，只需要把 B 上的 4 个盘子从 B -> C 就行。（这里的 pole1, 2, 3 分别就是 A, B, C 杆）

问题是仍要想办法如何移动上边的 4 个盘子，我们可以同样的方式来移动上边的 4 个盘子，这就是一种递归的解法。

给定 n 个盘子和三个杆分别是 源杆(Source), 目标杆(Destination)，和中介杆(Intermediate)，我们可以定义如下递归操作：

把上边的 n-1 个盘子从 S 移动到 I，借助 D 杆
把最底下的盘子从 S 移动到 D
把 n-1 个盘子从 I 移动到 D，借助 S
'''


def hanota_move(n, source, dest, intermediate):
	# 递归出口，只剩一个盘子
	if n >= 1:
		hanota_move(n - 1, source, intermediate, dest)
		print('Move %s -> %s' % (source, dest))
		hanota_move(n - 1, intermediate, dest, source)


hanota_move(64, 'A', 'C', 'B')
