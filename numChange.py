
B = 5
C = 10
D = 25

coinValues = [B,C,D]

def baseValue(i):
	return i//coinValues[0]+1

def getCoins(j):
	dimes = []
	quarters = []

	for i in range(0,C):
		dimes.append(baseValue(i))
		quarters.append(dimes[i])				
	
	for i in range(C,D):
		dimes.append(dimes[i-C]+baseValue(i))
		quarters.append(dimes[i])
	
	for i in range(D,j+1):
		dimes.append(dimes[i-C]+baseValue(i))
		quarters.append(dimes[i]+quarters[i-D])
	return quarters[j]

def getChange(j):
	
	#Matrix of all the coin values, starts from the second coin
	#Due to explicit value for first coin
	coins = []
	
	
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
		if(currCoin == 1):
			pass#return tempCoins[j]

	return coins[len(coins)-1][j]
Z = 100 
print(getCoins(Z))
print(getChange(Z))
def numNickels(i):
	dimes = [1]*5+[2]*5+[4]*5+[6]*5+[9]*5
	quarters = [1]*5+[2]*5+[4]*5+[6]*5+[9]*5
	for i in range(25,i+1):
		dimes.append(dimes[i-10]+i//5+1)
		quarters.append(dimes[i]+quarters[i-25])
	return quarters[i]
print(numNickels(Z))

