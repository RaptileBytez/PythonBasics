# ## MAP ###
# Map in Python is a function that works as an iterator to return a result after applying a function to
# every item of an iterable
def double_number(number: int) -> int:
    return number * 2


print(list(map(double_number, [1, 2, 3, 4])))

# Or as an one-liner to double the number of a list
print(list(map(lambda num: num * 2, [1, 2, 3, 4])))

# One liner to square
print(list(map(lambda res: res ** 2, [1, 2, 3, 4])))

### FILTER ###
# The filter() method filters the given sequence with the help of a function that tests each element in the
# sequence to be true or not
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
even_numbers = filter(lambda number: number % 2 == 0, numbers)
print(list(even_numbers))
