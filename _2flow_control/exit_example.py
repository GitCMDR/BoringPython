""" This module will test the sys.exit() function """

import sys

def exit_example():
    """This is a test of the sys.exit() function imported from 'sys' module"""
    while True:
        print('Type exit to exit')
        response = input()
        if response == 'exit':
            sys.exit()
        print('You typed ' + response + '.')

exit_example()
