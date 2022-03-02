"""
    Slicing
    General Syntax is
    l[startindex:lastindex + 1]
    Extends to the end if not given
"""

a = [0, "One",2,"Three",4,"five"]
print("1 to 3", a[1:4])
print("1 to end ",a[1:])
print("Beginning to 3",a[:4])
print("Complete Array",a[:])