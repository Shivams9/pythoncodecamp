cricketers = {"A", "C"}
footballers = {"B", "C"}
hockey = {"D", "C"}
u = cricketers.union(footballers).union(hockey)
print("Union  ", u)
i = cricketers.intersection(footballers).intersection(hockey)
print("Intersect ", i)
diff1 = cricketers.difference(footballers)
print("C-F", diff1)
diff1 = cricketers - footballers
print("C-F", diff1)
diff1 = cricketers.symmetric_difference(footballers)
print("C-F", diff1)

s={0,1,1,1,1,1,1}
s.add(1)
print(s)
