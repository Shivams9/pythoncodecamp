#increasing max value

a=[1,3,4,5,2,6,22,21,12]
minValue = a[0]
maxValue = a[0]
n = len(a)
for i in range(1,n):
    if a[i] > maxValue:
        maxValue = a[i]
        if a[i] < minValue:
            minValue =a[i]
print(maxValue)
print(minValuep)
