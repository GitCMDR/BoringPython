"""this module will explain how references are passed to functions in python"""

def eggs(some_parameter):
    """explaining how references are passed to function in python"""
    some_parameter.append('Hello')
    print(some_parameter)

spam = [1, 2, 3]
eggs(spam)
print(spam)
