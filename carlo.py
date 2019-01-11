import random


def hello(a):
	width = 0
	height = 0
	for i in range(a):
		walk = random.randrange(0,4,1)
		if walk == 0:
			height = height+1
		elif walk == 1:
			height = height-1
		elif walk == 2:
			width = width+1
		else:
			width = width-1
	return (width,height)
for i in range(1):
	step = hello(10)
	print(abs(step[0]+abs(step[1])))
