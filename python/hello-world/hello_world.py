#
# Skeleton file for the Python "Hello World" exercise.
#


def hello(name=''):
	return "Hello, World!" if name=='' else ("Hello, %s"%name)
	
if __name__=="__main__":
	print hello()
	print hello('oscar')