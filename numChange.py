from functools import *
from math import * 

from numpy import polyfit, corrcoef

coinValues = []

begin = 1
end = 100
step = 1

def calcR(s=True):
	global coinValues
	global begin
	global end
	global step

	values = []
	f = open("J.txt","a")
	for i in range(begin,end,step):
		if(s):
			values.append(getCoins(i) - getP(i))
		else:
			values.append(getCoins(i))
	if(s):
		curve = polyfit(list(range(begin,end,step)),values,2)
	else:
		curve = polyfit(list(range(begin,end,step)),values,3)
	curve = list(map(lambda x: float(round(x,5)),curve))
	if(s):
		r = corrcoef(values,list(map(lambda x: curve[0]*x**2+curve[1]*x+curve[2],list(range(begin,end,
		step)))))[0,1]
	else:
		r = corrcoef(values,list(map(lambda x: curve[1]*x**3+curve[1]*x**2+curve[2]*x+curve[3],list(range(begin,end,step)))))[0,1]
	if(s):
		curve = [round(getP(1),5)]+(curve)
	print(begin,end,curve,r)
	f.write(str(begin)+ " "+str(end) + " "+str(curve) + " " + str(r)+"\n")
	f.close()

def getP(i):
	p = 1
	for j in range(0,len(coinValues)):
		p*=(j+1)*(coinValues[j])
	return i**(len(coinValues))/p


def start():
	global coinValues	
	global begin
	global end
	global step
	command = input("> ")
	if(not(command == "q") and not(command == "quit")):
		if("am" in command):
			if(len(command.split()) == 2):
				coinValues = [5,10,25]
				print(getChange(int(command.split()[1])))
			elif command.split()[2].lower() == "t" or command.split()[2].lower() == "true":
				coinValues = [5,10,25,50]
				print(getChange(int(command.split()[1])))
		elif("ch" in command):
			coinValues = command.split()[2:]
			for i in range(0,len(coinValues)):
				coinValues[i]= int(coinValues[i])
			try:
				print(getChange(int(command.split()[1])))	
			except IndexError:
				print("Invalid Input, check if coin values are less than the change")			
		elif("cm" in command):
			calcR(False)
			calcR()
		elif("cl" in command):
			c = command.split()[1:]
			if(c!=[]):
				z = []
				for i in range(0,len(c)):
					z.append(int(c[i]))
				coinValues = z
			print(coinValues)
			endLoop = end+1
			beginLoop = begin
			for i in range(beginLoop,beginLoop+step):
				end+=1 	
				begin+=1	
				calcR()
	
		#Set Begin
		elif("sb" in command):
			begin = int(command.split()[1])
		elif("se" in command):
			end = int(command.split()[1])
		elif("ss" in command):
			step = int(command.split()[1])
		start()

def getChange(j):
	
	#Matrix of all the coin values, starts from the second coin
	#Due to explicit value for first coin
	coins = []
	
	if(len(coinValues) == 1):
		return j//coinValues[0]+1	
	
	for currCoin in range(0,len(coinValues)-1):
		tempCoins = []
		if(currCoin == 0):
			#Define base off of explict value
			#Upshift, because lowest value isn't counted in loop
			for i in range(0,coinValues[currCoin+1]):
				#Get all the values less than the coin values (like 1-9 for dime)
				tempCoins.append(i//coinValues[0]+1)
			for i in range(coinValues[currCoin+1],j+1):
				#Loop through the rest of the coins
				#Sum the basic value, with the coin value down shifted by itself
				tempCoins.append(i//coinValues[0]+1+tempCoins[i-coinValues[currCoin+1]])
		else:
			for i in range(0,coinValues[currCoin+1]):
				#Same as the value underneath it
				tempCoins.append(coins[currCoin-1][i])
			for i in range(coinValues[currCoin+1],j+1):
				tempCoins.append(tempCoins[i-coinValues[currCoin+1]]+coins[currCoin-1][i])				
						
		coins.append(tempCoins)

	return coins[len(coins)-1][j] 
def baseValue(i):
        return i//coinValues[0]+1

def getCoins(j):
        dimes = []
        quarters = []

        for i in range(0,10):
                dimes.append(baseValue(i))
                quarters.append(dimes[i])

        for i in range(10,25):
                dimes.append(dimes[i-10]+baseValue(i))
                quarters.append(dimes[i])

        for i in range(25,j+1):
                dimes.append(dimes[i-10]+baseValue(i))
                quarters.append(dimes[i]+quarters[i-25])
        return quarters[j]



print("""
Commands
q or quit: Exits the program
am [Integer Coin] [Opt. Boolean Half Dollar]: Gives change in American dollar, half dollar assumed to be false
ch [Integer Coin] [Coin Values]: Gives change based on coin values, everything seperated by a space
cm: Compares all the values until the coin with x^3/7500
cl: Calculates regression values until the end value
sb [Integer Value]: Sets the starting value for comparing
se [Integer Value]: Sets the ending value for comparing
ss [Integer Value]: Sets the step value for comparing
""")
start()

