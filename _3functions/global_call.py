"""this module presents the access to global variables via functions"""

def spam():
    """we will access global vaiable eggs"""
    global eggs
    eggs = 'spam'

# pylint: disable=c0103

eggs = 'global'
spam()
print(eggs)
