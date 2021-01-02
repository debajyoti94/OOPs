'''

-Creating a Class and setting a max size to the instance of that class
-The instance keeps the most recent elements that are pushed to it
-In this code we create a getter and setter method
'''

from DSDJ.OOP.Classes.assignments import MaxSizeList

a = MaxSizeList(1)
b = MaxSizeList(3)

a.push("hello")
a.push("hello")
a.push("hello")

b.push("is")
b.push("there")
b.push("anybody")
b.push("in")
b.push("there")

print(a.get_list())
print(b.get_list())