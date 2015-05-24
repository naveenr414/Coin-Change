def numChange(n,uses,listOfCoins):
	if(n<=4):
		return 1

	else:
		numPen = 1
		coins = [0]*len(uses)
		for i in range(0,len(uses)):
			if(uses[i]):
				for j in range(1,n//listOfCoins[i]+1):
					coins[i]+=numChange(n-j*listOfCoins[i],[False]*(i+1)+uses[(i+1):],listOfCoins)
		return 1+sum(coins)
print(100,numChange(100,[True]*4,[5,10,25,50]))
