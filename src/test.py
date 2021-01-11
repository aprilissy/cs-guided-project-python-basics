# print('hello world')

"""
a = 25
b = "Hi!"
c = 3.14159

print(a, b, c)

if a < 20:
  print('a is less than 20!')
elif a < 30:
  print('a is between 20 and 30')
else:
  print('a must be >= 30!')
"""

a = [11, 22, 33, 44]
# print(a)
# print(a[1])

a[2] = 999

'''
print(a)
print(a[1:3]) # slice - makes a copy of the list
print(a[1:])  # slice
print(a[:2])  # slice
print(a[:])   # make a copy of the list
'''

# for elem in a:
#   print(elem)

'''
for i, elem in enumerate(a):
  print(i, elem)
  # print(f"index {i} holds the value {elem}")
'''

'''
for i in range(len(a)):
  elem = a[i]
  print(i)
  # print(f"index {i} holds the value {elem}")
'''

def hello(x):
  print(f'x is {x}')

  return x + 10

print(hello(2))
print(hello(3))
