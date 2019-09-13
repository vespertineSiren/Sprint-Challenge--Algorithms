#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
while loop has will not run through every n element, this is linear runtime complexity


b) 
The outer loop (for i in range(n):) will be running in O(n) since it goes through every element without jumps. 
The inner loop is a while loop which is equivalent to a for loop so that is O(n) but that second loop is kinda ignoring with the exception of resetting j
So... I will go with O(n)


c) O(n)
recursive call algorithm. eventually resolves itself down before before returning an open call. only really calls itself once each time though. 

## Exercise II

This sounds like binary search. Split the floor in half, throw, check to see if it breaks. If it breaks check the middle half of the lower end if it doesnt check the upper half. 

The runtime complexity is O(logn)


