"""This is a code snippet to test while loop in Python"""

def normal_if():
    """This is a normal if statement"""
    spam = 0
    if spam < 5:
        print('Hello, world!')
        spam = spam + 1
        print('I have said this ' + str(spam) + ' times') # print how many
                                                          # times the statement has run
        print()

normal_if()

def while_loop():
    """This is a while loop"""
    spam = 0
    while spam < 5:
        print('Hello World')
        spam = spam + 1
        print('I have said this ' + str(spam) + ' times')
        print()

while_loop()
