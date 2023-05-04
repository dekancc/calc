math_type = input('Write a type of math ')
try:
    first = int(input('First number '))
    second = int(input('Second number '))
except ValueError:
    print("Invalid input: please enter integers only")
else:
    if math_type == '+':
        print('Your answer is: ', first + second)
    elif math_type == '-':
        print('Your answer is: ', first - second)
    elif math_type == '*':
        print('Your answer is: ', first * second)
    elif math_type == '/':
        if second == 0:
            print("Cannot divide by zero")
        else:
            print('Your answer is: ', first / second)
    else:
        print('Incorrect type, I support only "+", "-", "*", "/", I am not so strong :)')
