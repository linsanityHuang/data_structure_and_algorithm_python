



import math

def radix_sort(input_list, radix=10):
	'''
	基数排序
	将所有待比较数值（正整数）统一为同样的数位长度，数位较短的数前面补零。
	然后，从最低位开始，依次进行一次排序。这样从最低位排序一直到最高位排序完成以后，数列就变成一个有序序列。
	'''

	n = len(input_list)
	if n <= 1:
		return input_list
	k = int(math.ceil(math.log(max(input_list), radix)))
	for i in range(1, k+1):
		bucket = [[] for x in range(radix)]
		for val in input_list:
			bucket[val % (radix ** i) // (radix ** (i - 1))].append(val)
		del input_list[:]

		for each in bucket:
			input_list.extend(each)
	return input_list

if __name__ == '__main__':
	input_list = [472, 562, 794, 354, 587, 94, 467, 57, 418, 633, 928, 209, 607, 302, 478, 719, 876, 814, 70, 463]
	# input_list = list(np.random.randint(1,1000,20))
	print('排序前:', input_list)
	sorted_list = radix_sort(input_list)
	print('排序后:', sorted_list)