"""
This 'app' returns a grade depending on a score

This is an introduction to booleans, comparison and the if/elif/else code structure
"""

score = int(input('Please enter the score you got in the test: '))

# Now after the score has been assigned, let's rate it. This is done by the code block below. The print statement
# will only be executed, if the CONDITION is TRUE e.g. only if you got a score between 100 and 90, you will receive
# an A because the score is smaller than 100 and at the same time it is greater than 90

if score >= 100:
    print('Excellent! you got an A+')
elif 100 > score >= 90:  # <= This is the pythonic way of writing: elif score < 100 and score >= 90 which means you
    # are in fact chaining booleans
    print('A')
elif 90 > score >= 80:
    print('B')
elif 80 > score >= 70:
    print('C')
elif 70 > score >= 60:
    print('D')
elif 60 > score >= 50:
    print('E')
else:
    print('F')
