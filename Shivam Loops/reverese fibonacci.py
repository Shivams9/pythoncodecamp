#reverse fibonacci series
# 8,5,3,2,1,1,0
c = 21
b = 13
print(c, b)
a = c - b
while a > 0:
    print(a, end=" ")
    c = b
    b = a
    a = c - b
print(a)



#second program
a= 8
b= 0
n= 7
print()
output=""
print("0", ",",  end="")
for i in (range( n+1)):
    c = a + b
    a= b
    b= c

    output=str(c) +"." + output
    print(",", c, end="")
    print()
    print(output)

