"""This program says hello and asks for my name."""

def nameage():
    """This program asks for your name and then asks for your age and gives you age + 1"""
    print('Hello World!')
    print('What is your name?') # ask for their name
    my_name = input()
    print('It is good to meet you, ' + my_name)
    print('The length of your name is: ')
    print(len(my_name))
    print('What is your age?')  #ask for their age
    my_age = input()
    print('You will be ' + str(int(my_age) + 1) + ' in a year.')

nameage()
