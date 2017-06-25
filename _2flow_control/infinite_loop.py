"""This program wil create an infine loop"""

def infinite():
    "This function will create an infinite stream of Hello World"
    while True:
        print('Hello World!') # use control+C to send a keyboard
                              # interrupt and stop the loop!

infinite()
