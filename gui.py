from base import getChange
from stats import calcRegression, PRECISION
from util import lcm, factorial
import numpy
numpy.seterr(all='ignore')
coins = [1,5,10,25]

def lc(args):
	#Get the regression value for a list of coins


	start = int(args[0])
	step = int(args[1])
	iterations = int(args[2])
	end = start+step*iterations

	xAxis = list(range(start,end,step))
	yAxis = []

	for i in xAxis:
		yAxis.append(getChange(i,coins))

	r = calcRegression(xAxis,yAxis,len(coins)-1)
	c = r[0]
	r = r[1]		

	a = ""
	for i in range(0,len(c)):
		a+=str(c[i])+"x^"+str(len(c)-(i+1))+" "
	
	a+="\n"+str(r)	

	return a

def ap(args):
	f = open("dump.txt","w")
	start = int(args[0])
	iterations = len(coins)
	uniquePolys = int(lcm(coins))
	for i in range(start,start+uniquePolys*iterations):
		
		#Argument to Pass Into the LC Function (Starting Value,Step, Number of Iterations)
		passArg = [str(i),str(uniquePolys),str(iterations)]
		f.write(str(i%uniquePolys) + " "+lc(passArg).split("\n")[0] + "\n")	

def cs(args):
	#Compare to Schurs

	start = 1
	step = 1
	iterations = int(args[0])
	
	
	without = lc([start,step,iterations]).split("\n")[0]
	xAxis = list(range(1,1+iterations))
	yAxis = []

	productOfCoins = 1

	for i in range(0,len(coins)):
		productOfCoins*=coins[i]
	firstTerm = 1/(factorial(len(coins)-1)*productOfCoins)	
	degree = len(coins)-1
	
	for i in xAxis:
		yAxis.append(getChange(i,coins) - i**degree*firstTerm)
		
	reg = calcRegression(xAxis,yAxis,degree-1)[0]

	for i in reg:
		i = round(i,PRECISION)

	equation = str(round(firstTerm,PRECISION))+"x^"+str(degree) + " "
	for i in range(0,len(reg)):
		equation+=str(round(reg[i],5))+"x^"+str(degree-(1+i))
		equation+=" "
	return [without,equation] 	
	

def parse(command):
	global coins

	command = command.split()
	args = [""]
	if(len(command)>=2):
		args = command[1:]
	if(len(command)>=1):
		command = command[0]

	if(command == "gc"):
		c = int(args[0])
		print(getChange(c,coins))

	elif(command == "sc"):
		coins = []
		for i in range(0,len(args)):
			coins.append(int(args[i]))
		
		print("Current Coins",list(map(lambda x: print(x,end=" "),coins)))

	elif(command == "lc"):
		print(lc(args))


	elif(command == "ap"):
		ap(args)

	elif(command == "cs"):
		print(cs(args)[0])
		print(cs(args)[1])
#Where all the user input is taken
def mainLoop():
	print("gc, Get Coins\nsc, Set Coins\nlc, List Coins\nap All Polys\ncs Compare to Schurs")
	#Basic Command Line 
	command = input("> ")

	#Check if user wants to quit
	while(command.lower() not in ["q","quit","exit"]):
		parse(command)
		command = input("> ")

if(__name__ == "__main__"):
	mainLoop()
