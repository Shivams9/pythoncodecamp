#  fibonacci series at 7
a = 0
b = 1
n = 7

print("0", ",", 1, end="")
for i in (range(3, n + 1)):
    c = a + b
    a = b
    b = c
    print(",", c, end="")
print()

#reverse fibonacci series
# 8,5,3,2,1,1,0
c = 21
b = 13
print(c,b)
a = c - b
while a > 0:
    print(a, ",", end="")
    c = b
    b = a
    a = c - b
print(a)








