from random import randint
	
def dice(d):
    roll = [(randint(1,int(d)))]
    print(roll)
def times(x):
	r = 0
	d = input("How many sides?")
	while r != x:
		dice(d)
		r = r + 1

y = int(input('how many go arounds?'))

while y != 0:
    times(int(input("How many times?")))
    y -= 1
    print(y)
