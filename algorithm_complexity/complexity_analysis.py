def find(array, x):
	pos = -1
	for i, item in enumerate(array, start=0):
		if item == x:
			pos = i
			break
	return pos
