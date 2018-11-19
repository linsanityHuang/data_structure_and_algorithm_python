import array
'''
1.如何在一个1到100的整数数组中找到丢失的数字
'''

numbers = array.array('i', [1, 4, 6])
missing_numbers = []
print(numbers)
for i in range(1, 101):
	if i not in numbers:
		missing_numbers.append(i)
		

print(missing_numbers)

numbers = set(numbers)
print(set(range(1, 101)) - numbers)
