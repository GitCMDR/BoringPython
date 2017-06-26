"""this module will test how scopes interact with each other"""

def spam():
    """testing variable scope of bacon"""
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    """bacon will be used in spam"""
    ham = 101
    eggs = 0

spam()
