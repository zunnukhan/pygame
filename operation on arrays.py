import numpy as np

a=np.arange(9,dtype=np.float64).reshape(3,3)
print("first Array:")
print(a)
print("\n")

b=np.array([10,10,10])
print("Second Array")
print(b)
print("\n")

print("Add the two arrays:")
print(np.add(a,b))
print()

print("Subtract the two arrays:")
print(np.subtract(a,b))
print()

print("Multiply the two arrays:")
print(np.multiply(a,b))
print()

print("Divide the two arrays:")
print(np.divide(a,b))
print()