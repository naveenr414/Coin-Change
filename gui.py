from base import getChange
from stats import calcRegression
from util import lcm
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
		a+=str(c[i])+"x^"+str(len(c)-i)+" "
	
	a+="\n"+str(r)	

	return a

def ap(args):
	start = int(args[0])
	uniquePolys = int(lcm(coins))
	for i in range(start,start+uniquePolys+1):
		print(i%uniquePolys,lc([str(i),str(uniquePolys),str(len(coins)-1)]))	

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
#Where all the user input is taken
def mainLoop():

	#Basic Command Line 
	command = input("> ")

	#Check if user wants to quit
	while(command.lower() not in ["q","quit","exit"]):
		parse(command)
		command = input("> ")

if(__name__ == "__main__"):
	mainLoop()