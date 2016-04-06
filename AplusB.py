



'''Input a series of data, each series contain two numbers,
calculate the sum of each set'''

while True:
	try:
		(x,y) = (int(x) for x in raw_input().split())
		print x+y
	except EOFError:
		break


