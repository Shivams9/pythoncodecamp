# min and max value
a = [10, 34, 5, 6]
minValue = a[0]
maxValue = a[0]
n = len(a)
for i in range(1, n):
    if a[i] > maxValue:
        maxValue = a[i]
    if a[i] < minValue:
        minValue = a[i]
print(minValue, maxValue)
