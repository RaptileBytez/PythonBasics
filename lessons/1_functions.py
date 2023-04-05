# https://www.youtube.com/watch?v=B9nFMZIYQl0
# The following lines define various functions. Note the line indention.
# Everything indented under the function name is executed, when the function is called
def hello_world():
    """
    Function accepting no argument
    :return:
    """
    print('Hello world!')


# Function with an argument
def say_name(name: str) -> None:
    """
    Function taking one argument printing the name to the console
    :param name: String
    :return: None
    """
    print(name)


# Multiple arguments
def greeting(greet: str, name: str) -> None:
    """
    Function taking two arguments printing them to the console
    :param greet: String: Greeting used to greet
    :param name: String: Name of the person to greet
    :return: None
    """
    print(f'🖐 {greet} {name}!')


def greeting_with_default(name: str, greet='Aloha') -> None:
    """
    Function taking two POSITIONAL arguments printing them to the console, but in contrast to the function above,
    it has a preset greeting :param greet: String: Greeting used to greet :param name: String: Name of the person to
    greet :return: None
    """
    print(f'🖐 {greet} {name}!')


def weather_to_emoji(weather: str) -> None:
    """
    Function with embedded TYPEHINTING clearly documenting which type of arguments and return to expect from the function
    weather_to_emoji takes in 1 argument as a string
    (expected inputs: 'rain', 'thunderstorm', 'sunny', 'cloudy')
    It returns nothing

    :param weather: str
    :return: None

    >>> weather_to_emoji('rain')
    ☔
    """
    if weather == 'rain':
        print('☔')
    elif weather == 'cloudy':
        print('☁')
    elif weather == 'sunny':
        print('☀')
    elif weather == 'thunderstorm':
        print('🌩')
    else:
        print('❄')


def greater_int(a: int, b: int) -> int:
    """
    The function takes in 2 integer arguments and returns the greater one
    :param a:
    :param b:
    :return:

    >>> greater_int(2, 3)
    3
    """
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return a


def sum(a: int, b: int) -> int:
    """
    Function to calculate the sum of 2 given integers
    :param a:
    :param b:
    :return: Sum of a + b

    >>> sum(1, 2)
    3
    """
    return a + b

# say_name('Lola')


print('using the default greeting')
greeting_with_default('Lola')

print('positional arguments')
greeting_with_default('Lola', 'Hi')

print('named arguments')
greeting_with_default(greet='Hi', name='Lola')

print('weather_to_emoji Function: ')
weather_to_emoji('sunny')


# Lamda - anonymous functions
sum2 = lambda a, b: a + b
print('Result of Lamda function: ' + str(sum2(1, 3)))

print('Running comparison function')
res = greater_int(3, 5)
print(res)

# testing code


def test_sum() ->None:
    assert sum(2, 3) == 5, '❌ sum(2, 3) does not return 5 like it should'
    assert sum(-3, 3) == 0, '❌ sum(-3, 3) does not return 0 like it should'
    assert sum(-3, -3) == -6, '❌ sum(-3, -3) does not return -6 like it should'
    print('3/3 tests passed ✔')


print('Running tests...')
test_sum()
