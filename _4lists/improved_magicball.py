"""this module will improve upon last chapter magic8ball"""

import random

def improved_ball():
    """this will pass a list to the function"""
    messages = [
        'It is decidedly so',
        'Yes definitely',
        'Reply hazy, try again',
        'Ask again later',
        'Concentrate and ask again',
        'My reply is no',
        'Outlook not so good',
        'Very doubtful']

    print(messages[random.randint(0, len(messages) - 1)])

improved_ball()
