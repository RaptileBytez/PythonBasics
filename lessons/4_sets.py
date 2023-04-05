# SETS {} only contain unique values
numbers = {1, 2, 2}
print(numbers)  # prints {1, 2}

list1 = ['Ruby', 'Python', 'JAVA', 'Rust']
list2 = ['Ruby', 'Javascript', 'C++', 'C#', 'JAVA']

programming_languages = list1 + list2
print(programming_languages)  # Prints both list including duplicates

# Let's remove the duplicates by making a set:
pl_set = set(programming_languages)
print(pl_set)
print('GO' in pl_set)  # 👉 False
print('JAVA' in pl_set)  # 👉 True


def unique(array: []) -> []:
    """
    Function takes in a list and returns the same contents of the list but without any duplicate items
    :param array: List possibly containing duplicates
    :return: unique list
    >>> unique(['Ruby', 'Python', 'Ruby'])
    ['Ruby', 'Python']
    """
    array_set = set(array)
    return list(array_set)


print(unique(programming_languages))

# or as a lambda function:
uniq = lambda languages: list(set(languages))
print(uniq(['ruby', 'ruby', 'Python', 'Rust']))
