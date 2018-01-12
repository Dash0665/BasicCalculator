'''
+ for addition
- for subtraction
* for multiplication
/ for division
** for power
% for modulo
'''

# calc functions
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def power(num1, num2):
    return num1 ** num2

#main loops
while True:

    #menu
    print('\nSelect operation.')
    print('Add?')
    print('Subtract?')
    print('Multiply?')
    print('Divide?')
    print('Powers?')
    print('Exit?')

    #user input
    choice = input('\nWhat would you like to do: ').split()[0][0]

    # Choice opperations
    if choice == 'a':  # Addition
        num1 = float(input('\nEnter first number: '))
        num2 = float(input('Enter second number: '))
        print(num1, '+', num2, '=', add(num1, num2))

    elif choice == 's':  # Subtraction
        num1 = float(input('\nEnter first number: '))
        num2 = float(input('Enter second number: '))
        print(num1, '-', num2, '=', subtract(num1, num2))

    elif choice == 'm':  # Multiplication
        num1 = float(input('\nEnter first number: '))
        num2 = float(input('Enter second number: '))
        print(num1, 'x', num2, '=', multiply(num1, num2))

    elif choice == 'd':  # Divistion
        num1 = float(input('\nEnter first number: '))
        num2 = float(input('Enter second number: '))
        print(num1, "/", num2, "=", divide(num1, num2))

    elif choice == 'p':  # Powers
        num1 = float(input('\nEnter first number: '))
        num2 = float(input('Enter the power of the number: '))
        print(num1, '^', num2, '=', power(num1, num2))

    elif choice == 'e':  # Exit
        break

    else:  # if user doesn't enter a valid operator
        print('\nInvalid Selection! \n'
              'Please enter a valid operator!')
