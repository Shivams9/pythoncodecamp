# second min and  second max value
a = [10, 4, 15, 6]
# m1=10, m2=4, m1=15,m2=10
if a[0] > a[1]:
    max1 = a[0]
    max2 = a[1]
else:
    max1 = a[1]
    max2 = a[0]
n = len(a)
for i in range(2,n):
    value=a[i]
    if value>=max1:
        max2=max1
        max1=value
        continue
    if value>max2:
        max2=value
print(max1,max2)

#currentvalue>=max1 & currentvalue>=max2 and <max1
#print



