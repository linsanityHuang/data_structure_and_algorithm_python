'''
计算原列表中的偶数的平方并生成新的列表
'''

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 方法1
# 列表生成式
new_array = [x**2 for x in array if x % 2 == 0]
print(new_array)


# 方法2
# 生成器函数
def generator(array):
	for item in array:
		if item % 2 == 0:
			yield item ** 2

new_array = []

for item in generator(array):
	new_array.append(item)
	
print(new_array)

