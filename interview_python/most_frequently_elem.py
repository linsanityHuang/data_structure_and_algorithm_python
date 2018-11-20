import operator
from collections import Counter, defaultdict

'''
求数组中出现次数最多的元素
一共提供了四种方法
方法1: Counter
方法2: dict
方法3: defaultdict
方法4: 字典生成式及list.count()
'''

words = [
	'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
	'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
	'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
	'my', 'eyes', "you're", 'under'
]

'''
方法1
'''
# 使用collections中的Counter对象, 求出序列中出现次数最多的元素
print(Counter(words).most_common(1)[0])

'''
方法2
'''
# 使用普通字典统计元素出现次数
dict_num = {}
for item in words:
	if item not in dict_num.keys():
		dict_num[item] = 1
	else:
		dict_num[item] += 1
# 然后排序得到出现次数最多的元素
dict_num = sorted(dict_num.items(), key=operator.itemgetter(1), reverse=True)
print(dict_num[0])

'''
方法3
'''
# 使用defaultdict统计元素出现次数
dict_num_default = defaultdict(int)
for item in words:
	dict_num_default[item] += 1
dict_num_default = sorted(dict_num_default.items(), key=operator.itemgetter(1), reverse=True)
print(dict_num_default[0])

'''
方法4
'''
dict_num = {i: words.count(i) for i in set(words)}
print(sorted(dict_num.items(), key=operator.itemgetter(1), reverse=True)[0])
