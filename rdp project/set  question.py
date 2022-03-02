a = {'C', 'C++', 'Java'}

b = {'C++', 'Java', 'Python'}

c = {'java', 'Python', 'C', 'pascal'}
# who known all three subject
u = a.union(b).union(c)
print("Union", u)
# find subject known to A and not to B
i = a.intersection(b)
print("Intersection", i)
diff1 = a.difference(b)
print(a, b, "C-F", diff1)



#find a subject who only know only one student
studentswhoknowonlypascal=[]
if "pascal " in a:
    studentswhoknowonlypascal.append("A")
if "pascal" in b:
    studentswhoknowonlypascal.append("B")
if "pascal" in c:
    studentswhoknowonlypascal.append("C")
print(studentswhoknowonlypascal)





# find a student who only know Python

studentswhoknowpython=[]
if "Python" in a:
    studentswhoknowpython.append("A")
if "Python" in b:
    studentswhoknowpython.append("B")
if "Python" in c:
    studentswhoknowpython.append("C")
print(studentswhoknowpython)


#find subject who known all three
i = a.intersection(b).intersection(c)
diff1 = a.difference(b).difference(c)
print("C-F", diff1)
