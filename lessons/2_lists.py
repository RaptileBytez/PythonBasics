# Lists
fruits = ['🍎', '🍐', '🍊', '🍌']
print(fruits)

# Use Method append to add another fruit
fruits.append('🍓')
print(fruits)

# INDEXING Each item has and index. The items of the fruits each have a number (index) starting from 0, enabling you
# to access a specific item. e.g. you can print out the orange by using
print(fruits[2])  # prints the orange

# You ALWAYS get the LAST item of a list by calling the index -1
print(fruits[-1])

# SLICING
print(fruits[0:3])  # 1st index is inclusive, 2nd is exclusive

# How to print list containing an UNKNOWN number of items
print(fruits[0: len(fruits)])  # The len() function is used to return the length of the list

# You can also iterate through lists using a certain STEP.
print(fruits[0:len(fruits):2])
# e.g. you can reverse the list using SLICING
reverse_fruits = fruits[::-1]
print(reverse_fruits)

# Dictionary
def computer_to_string():
    computer = {
    'manufacturer': 'Sony',
    'type': 'Console',
    'name': 'PlayStation 5',
    'CPUcores': 4,
    'GPUcores': 4,
    'totalCores': lambda: computer['CPUcores'] + computer['GPUcores']
    }
    print(f"This {computer['type']} is a {computer['manufacturer']} {computer['name']} and has {computer['totalCores']()} cores")
    print(list(computer.keys()))
    print(list(list(computer.values())))

computer_to_string()
