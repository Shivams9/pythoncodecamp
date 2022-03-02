"""
The range function returns an iterator which can be used for looping through.
Syntax of the range function is
range(start (default=0, end required, step default=1)
range(10) will loop from 0 to 9 onestep at a time 0,1,2,3,4,5,6,7,8,9, range(n) will go from 0 to n-1

range(2,5)  will go 2,3,4, range(start,end) will begin at start and go up to end-1
range(3,10,2) will go from 3 to 9 step size 2
3,5,7,9
range(3,9,2)  3,5,7,
"""
for i in range(10):
    print(i, ",", end="")
print()
n = 6
for i in range(n):
    print(i, ",", end="")
print()
n=3
for i in range(n):
    print(i, ", " ,end="")
print()


