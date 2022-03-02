"""Set theory """

s1 = set([1, 2, 3, 4, 4, 4, 2])
s2 = set([1, 2, 3, 4])
print(s1, s2)
print(type(s1), type(s2))
s1.add(5)  # add value
print(s1)
s1.update([1, 2, 3, 4, 5, 6, 7, 8])  # update
print(s1)
s1.remove(4) #remove data which in the line otherwise error
print(s1)
s1.discard(5) #remove data whatever you want it won't be error
print(s1)
poppedelement = s1.pop()
print(s1,poppedelement)
s1.clear()


