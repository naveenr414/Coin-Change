# Coin-Change

A Program that calculates the amount of change that can be made for a set of coins. For Example, the amount of change that can be made with Pennies, Nickels, Dimes and Quarters (or 1,5,10 and 25 cent coins), for 100 cents is 242. 

## Architecture

The Main file (gui.py), handles user interface. Calls are made to the base file for any calculations (like Change, Schurs, etc.). The stats file is used for calculating regression, and any other statistical needs. The util file helps for minor math algorithms, like calculating LCM for the leading term in Schur's Theorem. 

## Commands

gc, sc, lc, ap, cs, 

GC [Coin] - Calculates number of ways change can be made for the given coins

SC [Coin Value 1,Coin Value 2...] - Sets the current coin denomination

LC [Start] [Step] [Iterations] - Calculates the polynomial that fits the curve given by the amount of change at each of the points

AP [Start] - Calculates all of the unique polynomial, same as running LC starting at [Start] with Step of 1, for LCM of coins number of times. 

CS [Amount] - Compares the polynomial calculated with and without schurs theorem for the given amount 
