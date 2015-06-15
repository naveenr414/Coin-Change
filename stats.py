from numpy import corrcoef, polyfit
import numpy

#How many decimal places will the coefficient go to
PRECISION = 5 
numpy.seterr(all = 'ignore')

def calcRegression(xAxis,yAxis,degree):

	#Get the Polynomial that fits the list of degree N
	curve = list(polyfit(xAxis,yAxis,degree))		

	#Get the expected value from the curve for all Y Values
	expectedValues = []
	for i in range(0,len(xAxis)):
		expectedNumber = 0
		for j in range(0,len(curve)):
			#Go through each number in the curve, and raise it to the appropriate degree
			#Like for [5,2,3], degree = 2, then 5*x^2 + 2*x + 3, looping through coefficients		
	
			expectedNumber+=curve[j]*(xAxis[i]**len(curve)-2)
				
		expectedValues.append(expectedNumber)	

	#Calculate the R Value, difference between actual values and expectedValues
	r = corrcoef(yAxis,expectedValues)[0,1]

	for i in range(0,len(curve)):
		curve[i] = round(curve[i],PRECISION)

	return [curve,r]

if(__name__ == '__main__'):
	print(calcRegression([1,2,3],[0,1,2],1))
