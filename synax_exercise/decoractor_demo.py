from functools import wraps


def log(func):
	@wraps(func)
	def decoractor(*args, **kwargs):
		print('%s is running' % func.__name__)
		result = func(*args, **kwargs)
		return result
	return decoractor


def log(text):
	def decoractor(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			print('the paras is %s' % text)
			print('%s is running' % func.__name__)
			result = func(*args, **kwargs)
			return result
		return wrapper
	return decoractor


@log('tom')
def test(name):
	print('i am %s' % name)


if __name__ == '__main__':
	print(test)
	test('justin')
