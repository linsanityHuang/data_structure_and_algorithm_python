from collections import deque

graph = {'A': set(['B', 'C']),
		 'B': set(['A', 'D', 'E']),
		 'C': set(['A', 'F']),
		 'D': set(['B']),
		 'E': set(['B', 'F']),
		 'F': set(['C', 'E'])}

def dfs(graph, start):
	visited, stack = set(), [start]
	while stack:
		vertex = stack.pop()
		if vertex not in visited:
			visited.add(vertex)
			stack.extend(graph[vertex] - visited)
	return visited

dfs(graph, 'A')

def dfs(graph, start, visited=None):
	if visited is None:
		visited = set()
	visited.add(start)
	for next in graph[start] - visited:
		dfs(graph, next, visited)
	return visited

dfs(graph, 'C')

def dfs_paths(graph, start, goal):
	stack = [(start, [start])]
	while stack:
		(vertex, path) = stack.pop()
		for next in graph[vertex] - set(path):
			if next == goal:
				yield path + [next]
			else:
				stack.append((next, path + [next]))

list(dfs_paths(graph, 'A', 'F'))

def dfs_paths(graph, start, goal, path=None):
	if path is None:
		path = [start]
	if start == goal:
		yield path
	for next in graph[start] - set(path):
		yield from dfs_paths(graph, next, goal, path + [next])

list(dfs_paths(graph, 'C', 'F'))

def bfs(graph, start):
	visited, queue = set(), [start]
	while queue:
		vertex = queue.pop(0)
		if vertex not in visited:
			visited.add(vertex)
			queue.extend(graph[vertex] - visited)
	return visited

bfs(graph, 'A')

def bfs_paths(graph, start, goal):
	queue = [(start, [start])]
	while queue:
		(vertex, path) = queue.pop(0)
		for next in graph[vertex] - set(path):
			if next == goal:
				yield path + [next]
			else:
				queue.append((next, path + [next]))

list(bfs_paths(graph, 'A', 'F'))

def shortest_path(graph, start, goal):
	try:
		return next(bfs_paths(graph, start, goal))
	except StopIteration:
		return None
shortest_path(graph, 'A', 'F')

def person_is_seller(name):
	'''
	检查人的姓名是否以m结尾：如果是，他就是芒果销售商
	'''
	return name[-1] == 'm'

def search(graph):
	search_queue = deque()
	search_queue += graph						# deque(['you', 'bob', 'alice', 'claire', 'anuj', 'peggy', 'thoma', 'jonny'])
	searched = []								# 这个数组用于记录检查过的人
	while search_queue:							# 只要搜索队列不为空
		person = search_queue.popleft()			# 就取出其中的第一个人
		if person not in searched:				# 仅当这个人没检查过时才检查
			if person_is_seller(person):			# 检查这个人是否是芒果销售商
				print(person + " is a mango seller!")	# 是芒果销售商
				return True
			else:
				search_queue += graph[person]		# 不是芒果销售商。将这个人的朋友都加入搜索队列
				searched.append(person)				# 将这个人标记为检查过
	print("你的朋友圈里没有芒果销售商！")
	return False								# 如果到达了这里，就说明队列中没人是芒果销售商

# if __name__ == '__main__':
# 	# # {'刷牙': ['吃早餐'], '打包午餐': [], '起床': ['锻炼', '刷牙', '打包午餐'], '锻炼': ['洗澡', '穿衣服']}
# 	# graph = {}
# 	# # 添加你的邻居
# 	# graph["you"] = ["alice", "bob", "claire"]

# 	# # 添加你邻居的邻居
# 	# graph["bob"] = ["anuj", "peggy"]
# 	# graph["alice"] = ["peggy"]
# 	# graph["claire"] = ["thoma", "jonny"]
# 	# graph["anuj"] = []
# 	# graph["peggy"] = []
# 	# graph["thoma"] = []
# 	# graph["jonny"] = []
# 	# print(graph)
# 	# search(graph)