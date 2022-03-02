'''
Write a Python function to calculate the factorial of a number
(a non-negative integer). The function accepts the number as an argument.'''


def factorial(n):
    f = 1
    for i in range(1,n + 1):
        f = f * i
    return f

print(factorial(3))
