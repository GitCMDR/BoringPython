"""this module will present how exception handling is done in python"""

def spam(divide_by):
    "this function will divide by zero and it will catch the exception"
    try: # you use try when you think there is a potential error in code
        return 42 / divide_by
    except ZeroDivisionError: # this catchs the exception but you have to say what to catch
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0)) # this causes the error! but it should be catched and jump to next code line
print(spam(1))

def spam2(divide_by):
    "this will put the 'try' and 'except' outside function"
    return 42 / divide_by

try:
    print(spam2(2))
    print(spam2(12))
    print(spam2(0)) # this causes the error! but it should be catched and jump to next code line
    print(spam2(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')
