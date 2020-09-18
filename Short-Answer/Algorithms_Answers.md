#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This will loop n times so it should have a run time of O(n)


b) This has no interaction with the i so it appears to be O(n^2) n squared


c) This appears to have a constant run time using recursion O(c)

## Exercise II

So we have eggs which should have a attribute of broken or not broken. 

eggs.broken = True / False

n floors should probably be a list

index of n can equal the floor so we check 

now a function might be toss eggs

if the index of n >= f

then eggs.broken = True

eggs counter += 1

we should then go to the midpoint of n and check if eggs.broken = True

if so go to the midpoint of the left(lower values) if not go higher

check the midpoint again to see if they break and then go higher or lower

this should be able to locate f when the list is only 2 remaining and you 
return the highest value.

