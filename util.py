from functools import reduce

def factorial(n):
	l = 1
	for i in range(n,0,-1):
		l*=i
	return l

def lcmm(x,y):
    tmp=x
    while (tmp%y)!=0:
        tmp+=x
    return tmp

def lcm(args):
    return reduce(lcmm,args)

if(__name__ == "__main__"):
	print(lcm([6,2,5]))
