a = {1,2,3,4}
b = {1,2,3,4}
c = a

print("ID of a",id(a))
print("ID of b",id(b))
print("ID of c",id(c))
print(a is b)
print(a is c)
print(a is not b)
print(a is not c)
print(b is c)
print(b is not c)
