"""This is an example to explain indentation"""

def indentation():
    """check if name evaluates to mary and password evaluates to swordfish"""
    name = input()
    if name == 'Mary': # we open conditional
        print('Hello Mary') # we print message
        password = input()
        if password == 'swordfish': # if previous line evaluates to true run this block of code
            print('Access granted.')
        else:
            print('Wrong password.')

indentation()
    