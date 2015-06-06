from base import *

coins = [1,5,10,25]

def parse(command):
	global coins

	command = command.split()
	args = [""]
	if(len(command)>=2):
		args = command[1:]
	if(len(command)>=1):
		command = command[0].lower()

	if(command == "gc"):
		c = int(args[0])
		print(getChange(c,coins))

	elif(command == "sc"):
		coins = []
		for i in range(0,len(args)):
			coins.append(int(args[i]))
		
		print("Current Coins",list(map(lambda x: print(x,end=" "),coins)))

	elif(command == "lc"):
		print(lc(coins,args))


	elif(command == "ap"):
		ap(coins,args)

	elif(command == "cs"):
		
		schurResult = cs(coins,args)

		#Value from Schur's Theorem
		print(schurResult[0])
		
		#Value from Regression
		print(schurResult[1])
	elif(command == "h"):
		print("GC [Amount], returns amount of change for amount")
	
#Where all the user input is taken
def mainLoop():
	
	print("gc, Get Coins\nsc, Set Coins\nlc, List Coins\nap All Polys\ncs Compare to Schurs\nh Help")
	
	#Basic Command Line 
	command = input("> ")

	#Check if user wants to quit
	while(command.lower() not in ["q","quit","exit"]):
		parse(command)
		command = input("> ")

if(__name__ == "__main__"):
	mainLoop()
