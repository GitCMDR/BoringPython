"""This module will loop until the password 'swordfish' is given"""

def password_loop():
    """this is a loop example that will use 'continue' and 'break'"""
    while True:
        print('Who are you?')
        name = input()
        if name != 'Joe': # if user has input Joe continue the loop
            continue
        print('Hello, Joe. What is your password? (It is a fish...)')
        password = input()
        if password == 'swordfish': # if user has input swordfish break the loop
            break
    print('Access granted.')

password_loop()
