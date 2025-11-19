#Data Types
# Int - 123
# Float - 123.0
# String - "hello"
# Boolean - True, False

print("Hello")

# Input
a = 23
# name = input("Name= ")
# print(name)

# Math
divide = 9 / 3 # 3.0
divide = int(9 / 3) # 3
divide = 10 // 3 # 3, similar cu Math.floor()

# String methods
h = "hello"
upper_hello = h.upper()
h.find("e") # return index or -1
h.index("l") # return index or ValueError

age = 36
txt = f"My name is John, I am {age}"

crazy = "hh" * 3

x = 1 and 2 or 4 or (not 3)

# Array and Tuple 

x = [2, 3, 4, 5, 6]
x.append(1)
last = x.pop()
fist = x.pop(0)

copy = x[:]

t = (1, 3, 2, 5) # tuple, imutable list

for i in range(10):
    print(i, end=" ")
print()

for i in [1, 2, 3, 4, 5]:
    print(i, end=" ")
print()

for i, element in enumerate([1, 2, 3, 4, 5]):
    print(i, element, end=", ")
print()

reverse_list = x[::-1]

# Set
x = set()
x.add(5)
x.add(2)
x.remove(5)
exist = 4 in x # not in

# Dictionaire (HashMap)
x = {} # {'key': value}
x['key'] = 1
exist = 'key' in x

l = list(x.values())
del x['key']

for key, value in x.values():
    print(key, value)

