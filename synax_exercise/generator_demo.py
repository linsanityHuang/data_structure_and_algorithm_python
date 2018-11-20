from functools import wraps


def coroutine(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		g = func()
		next(g)
		return g
	return wrapper


@coroutine
def averagor():
	count = 0
	total = 0.0
	average = None
	while True:
		item = yield average
		count += 1
		total += float(item)
		average = total / count


if __name__ == '__main__':
	g = averagor()
	# next(g)
	g.send(1)
	g.send(2)
	print(g.send(3))
