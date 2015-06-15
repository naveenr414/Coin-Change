from base import *
import stats

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
		
		print("Current Coins",*coins,sep=" ")

	elif(command == "lc"):
		if(len(args)!=3):
			print("Invalid input, must be in form [Begin],[Step],[Iterations]")
		else:
			print(lc(coins,args))
	elif(command == "ap"):
		ap(coins,args)

	elif(command == "cs"):
		
		schurResult = cs(coins,args)

		#Value from Schur's Theorem
		print(schurResult[0])
		
		#Value from Regression
		print(schurResult[1])
	elif(command == "h" and len(args) == 0):
		print("GC [Amount], returns amount of change for amount")
	
	elif(command == "h"):
		try:
			f = open("res/"+str(args[0])+".txt","r")
			print(f.read(),end="")
		except FileNotFoundError:
			print("No Command '"+str(args[0])+"'")

	elif(command == "pc"):
		print(*coins,sep=" ")
		
#Where all the user input is taken
def mainLoop():
	
#	print("gc, Get Coins\nsc, Set Coins\nlc, List Coins\nap All Polys\ncs Compare to Schurs\nh Help")
#	print("pc, Print Coins")
	
	print(open("res/instructions.txt","r").read(),end="")	

	#Basic Command Line 
	command = input("> ")

	#Check if user wants to quit
	while(command.lower() not in ["q","quit","exit"]):
		parse(command)
		command = input("> ")

if(__name__ == "__main__"):
	mainLoop()
