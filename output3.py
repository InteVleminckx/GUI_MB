import math

class A:
	def function(self):
		pass

a = 0
b = 10

if a < b:
	print(b)
elif a > b or a == b:
	print(a)
else:
	print("equal")

while a != b:
	print(a)
	a += 1

for i in range(a):
	b += i
	print(b)
