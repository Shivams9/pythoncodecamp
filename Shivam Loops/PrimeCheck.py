"""
Prime Number
A prime number is a number that is only divisible by 1 and itself.
In other words a prime number is not divisible by any other number except one and itself.

Example
N=36
Factors  of 36 are
36      2   x   18
36      3   x   12
36      4   x   9
36      6   x   6  Square root
36      9   x   4
36      12  x   3
36      18  x   2

48      2   X   24
48      4   x   12
48      6   x   8
48      8   x   6
48      12  x   4
48      24  x   2

So, number cannot be divided by any number if not divisible up to square root

Steps
1. Input N
2. Find square root of N. Store in limit
3. Run a loop for i from 2 to limit
4. Try dividing N by i.If remainder is zero then print not prime. End loop
5. If loop ends without dividing print prime
"""
