from stats import calcRegression,PRECISION
from util import lcm,factorial

def lc(coins,args):
	#Get the regression value for a list of coins

	#Calculates for a range of values
	start = int(args[0])
	step = int(args[1])
	iterations = int(args[2])
	end = start+step*iterations

	xAxis = list(range(start,end,step))
	yAxis = []

	#Create the amount of change
	for i in xAxis:
		yAxis.append(getChange(i,coins))

	regression = calcRegression(xAxis,yAxis,len(coins)-1)
	

	coef = regression[0]
	#Pearson R Value between [-1,1]
	r = regression[1]		

	#Create the equation based on the coefficients
	equation = ""
	for i in range(0,len(coef)):
		#The last term is x^0, so subtract 1
		equation+=str(coef[i])+"x^"+str(len(coef)-(i+1))+" "
	
	#Add the R Value
	equation+="\n"+str(r)	

	return equation

def ap(coins,args):
	f = open("dump.txt","w")
	start = int(args[0])
	iterations = len(coins)
	uniquePolys = int(lcm(coins))
	for i in range(start,start+uniquePolys*iterations):
		
		#Argument to Pass Into the LC Function (Starting Value,Step, Number of Iterations)
		passArg = [str(i),str(uniquePolys),str(iterations)]
		f.write(str(i%uniquePolys) + " "+lc(coins,passArg).split("\n")[0] + "\n")	

def cs(coins,args):
	#Compare to Schurs

	start = 1
	step = 1
	iterations = int(args[0])
	
	
	without = lc(coins,[start,step,iterations]).split("\n")[0]
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

def getChange(coin,coinValues):
	#Make a reference table with the amount of change for each coin
	
	base = []
	for i in range(0,coin+1):
		#Determine if using only base coins, change can be made
		#Like for change for 99 cents, can it be made for 2 cents (No)
		if(i%coinValues[0]) == 0:
			#Change can be made using only Pennies (Or 2 cent...)
			base.append(1)
		else:
			base.append(0)
	
	#List of changes for each coin
	#Matrix of length Coins by Change
	coinMatrix = [base]	
	

	#We already figured out change for the base value
	for currCoin in range(1,len(coinValues)):
	
		#Change values for current 
		currentChange = []

		#1 Way to make change for 0 cents
		for currValue in range(0,coin+1):

			if((currValue)<coinValues[currCoin]):
				#For all coins less than the value (like 15 for a quarter)
				#Change is just number of ways with dimes (because 0 for quarter)
				currentChange.append(coinMatrix[currCoin-1][currValue])
			else:
				#Number of Change = Dn = Dn-25 (Or Coin Value) + Cn
				change = currentChange[currValue-coinValues[currCoin]]
				change+= coinMatrix[currCoin-1][currValue]
				
				currentChange.append(change)
		coinMatrix.append(currentChange)
	return coinMatrix[len(coinValues)-1][coin]

if(__name__ == "__main__"):
	print(getChange(100,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
