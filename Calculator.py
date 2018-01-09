'''
+ for addition
- for subtraction
* for multiplication
/ for division
** for power
% for modulo
'''
def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 // num2

def power(num1,num2):
    return num1 ** num2

#main loop
while True:
    print('\nSelect operation.')
    print('1.Add')
    print('2.Subtract')
    print('3.Multiply')
    print('4.Divide')
    print('5.Powers')
    print('6.Exit')

    choice = input('\nEnter choice(1/2/3/4/5/6): ')

    if choice == '6':
        break
               
    if choice == '1':
        num1 = int(input('\nEnter first number: '))
        num2 = int(input('Enter second number: '))
        print (num1, '+', num2, '=', add(num1,num2))

    elif choice == '2':
        num1 = int(input('\nEnter first number: '))
        num2 = int(input('Enter second number: '))
        print (num1, '-', num2, '=', subtract(num1,num2))

    elif choice == '3':
        num1 = int(input('\nEnter first number: '))
        num2 = int(input('Enter second number: '))
        print (num1, 'x', num2, '=', multiply(num1,num2))

    elif choice == '4':
        num1 = int(input('\nEnter first number: '))
        num2 = int(input('Enter second number: '))
        print(num1, "/", num2, "=", divide(num1,num2))

    elif choice == '5':
        num1 = int(input('\nEnter first number: '))
        num2 = int(input('What is the power of this number: '))
        print (num1, '^', num2, '=', power(num1,num2))

    elif choice == '6':
        break

    else:
        print('\nInvalid Selection!\n Please choise a number between 1-5')
