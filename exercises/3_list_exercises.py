# Lists and Loops exercises

def double(array: list) -> list:
    """
    The function doubles the number of each member of the list    :param array:  of number
    :return: List of numbers

    >>> double([1, 2, 3, 4, 5])
    [2, 4, 6, 8, 10]
    """
    result = []
    for number in array:
        res = number * 2
        result.append(res)
    return result


print(double([1, 2, 3, 4, 5]))


def count_words(string: str) -> int:
    """
    Count words function should return the number of words in a given string
    :param string: String you want to parse for the word count
    :return: Number of words of that string
    >>> count_words('Hello world how are you today')
    6
    """
    return len(string.split(" "))


print(f"The number of words of the sentence is {count_words('Hello world how are you today')}")


def sum_list(numbers: list[int]) -> int:
    """
    Sums up the numbers of the list and returns the sum
    :param numbers: List of numbers
    :return: Sum
    >>> sum_list([1, 2, 3])
    6
    """
    sum = 0
    for number in numbers:
        sum += number
    return sum


print(sum_list([1, 2, 3]))


def find_max(numbers: list[int]) -> int:
    """
    Returns the maximum number of a list of numbers
    ℹ Note: There is a Python built-in max() function, but you should not use it in order to practice lists & loops
    :param numbers: List of numbers
    :return: Maximum number
    >>> find_max([1, 5, 10, 3])
    10
    """
    current_max = numbers[0]
    for number in numbers:
        if number > current_max:
            current_max = number

    return current_max


print(find_max([1, 5, 10, 3]))

def word_frequency(phrase: str) -> dict:
    """
    This function returns a dictionary listing the words of the phrase and their word count
    :param phrase: Phrase to inspect
    >>> word_frequency('I love Batman because I am Batman')
    :return: Dictionary with word count
    {'I': 2, 'love': 1, 'Batman': 2, 'because': 1, 'am': 1}
    """
    result = {}
    words = phrase.split()
    for word in words:
        if word not in result:
            result[word] = 1
        else:
            result[word] += 1
    return result


print(word_frequency('I love Batman because I am Batman'))
