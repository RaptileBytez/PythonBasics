### LIST COMPREHENSIONS ###
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(numbers)

# as a filter
even_numbers = [number for number in numbers if number % 2 == 0]  # create a list of numbers by checking %2 == 0 for
# each number in the numbers list
print(even_numbers)

# you can also use a list comprehension like a map
doubled_numbers = [number * 2 for number in numbers]
print(doubled_numbers)

# odd numbers:
odd_numbers = [number for number in numbers if number % 2 == 1]
print(odd_numbers)
