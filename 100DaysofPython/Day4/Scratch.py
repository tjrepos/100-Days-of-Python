# Randoms & Lists
import my_module
import random

print(f"your random number between 1 - 10 is....  {random.randint(1, 10)}")

random_integer = random.randint(1, 10)

print(f"Your second random integer between 1 - 10 is.... {random_integer}")

print(f"My favourite number is {my_module.my_favourite_number}")

print(f"A random float between 0 and 1 is {random.random()}")

random_float = random.random()
print(f'Another random float between 0 and 1 is {random_float}')

random_float_10 = random.random() * 10
print(random_float_10)

random_float_uniform = random.uniform(1, 10)
print(random_float_uniform)



