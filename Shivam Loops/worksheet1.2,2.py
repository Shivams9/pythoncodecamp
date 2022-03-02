'''Two different numbers are called amicable numbers if the sum of the proper divisors of each is equal
to the other number. For example 220 and 284 are amicable numbers. Sum of proper
 divisors of 220 = 1+2+4+5+10+11+20+22+44+55+110 = 284 Sum of proper divisors
 of 284 = 1+2+4+71+142 = 220 Write a function to print pairs of amicable numbers in a range.

'''
def properdivisorssum(n):
    total = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            total += i
    return total


def findAmicable(start, end):
    a = []
    for i in range(start, end):
        for j in range(i + 1, end + 1):
            if properdivisorssum(i) == j and properdivisorssum(j)==i:
                a.append([i, j])
    return a


output = findAmicable(0, 1000)
print(output)
