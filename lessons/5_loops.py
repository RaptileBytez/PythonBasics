# Loops are handy when you want to perform the same action over and over again e.g. if you would want to print the
# word fruit followed by each member of a list followed by its index you would
fruits = ['🍎', '🍐', '🍊', '🍌']

#FOR LOOP
for fruit in fruits:
    print('fruit:', fruit, fruits.index(fruit))

# or using tuples created by the enumerate function:
for fruit in enumerate(fruits):
    print('fruit:', fruit[1], fruit[0])

# However, the code above is a bit clumsy. The cleaner way would be using tuple unpacking like this:
for index, fruit in enumerate(fruits):
    print('fruit:', fruit, index)

# You can also execute a loops a certain number of times using the range function e.g. add 10 Melons
for _ in range(10):
    fruits.append('🍉')

for index, fruit in enumerate(fruits):
    print('fruit:', fruit, index)

# WHILE LOOP
# ⚠ watch out for INFINITE LOOPs
# 👉 you must define a breaking condition in order to terminate the loop. If you don't, the loop will run forever!
counter = 0
while counter <= 10:
    print(counter)
    counter += 1

