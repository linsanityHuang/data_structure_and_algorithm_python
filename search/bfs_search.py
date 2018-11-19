from collections import deque

graph = {}
graph[3] = [3, 4]
graph[2] = [7, 8]
graph[4] = [9, 10]
graph[7] = []
graph[8] = []
graph[9] = []
graph[10] = []
print(graph)
search_queue = deque()
search_queue += graph
searched = []
flag = 1
print(search_queue)
while search_queue:
	item = search_queue.popleft()
	if item not in searched:
		if 9 == item:
			print("get item")
			flag = 0
			break
		else:
			search_queue += graph[item]
			searched.append(item)
if flag:
	print("not get item")

