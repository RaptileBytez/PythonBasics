# Tuples are immutable, meaning they cannot be updated or changed
numbers = (1, 2)
print(f'numbers is {type(numbers)} and is {numbers}')

# You can access a tuple by its index
print(numbers[0])  # prints 1
# but the following line gives you an error
# numbers[0] = 2
