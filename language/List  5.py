#Negative indexing

l = [0, "one", 2, "Three", 4,"Five"]

print("Last 2 element",l[-2:])
print(l)

print("2 from last to 4 from last",l[-4:-1])
print(l)

#General Syntax
print("2 from last to 4 from last ",l[-4:2 + 1])
print(l)