"""this module will resolve the challenge of chapter 3"""

def collatz(number):
    """this is the code of the challenge of chapter 3"""
    if number % 2 == 0:
        print('Your number is: ' + str(number))
        return number // 2

    elif number % 2 == 1:
        print('Your number is: ' + str(number))
        number = 3 * number + 1
        return number

def main():
    """main method"""
    while True: # this will keep retrying until code succeds
        try:
            my_number = int(input('Hey! Welcome! Enter a number: '))
        except ValueError:
            print('Please input an integer!')
            continue # part of the code to keep truing
        break # part of the code to keep trying

    while my_number != 1:
        my_number = collatz(int(my_number))
    print('Finally, your number has been rounded down to ' +
          str(my_number) + '!')

main()
