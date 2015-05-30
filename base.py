def getChange(coin,coinValues):
	#Make a reference table with the amount of change for each coin
	
	base = []
	for i in range(0,coin+1):
		#Determine if change can only be made with the base coin
		if(i%coinValues[0]) == 0:
			#Change can be made using only Pennies (Or 2 cent...)
			base.append(1)
		else:
			base.append(0)
	
	#List of changes for each coin
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
