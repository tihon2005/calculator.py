print('Enter 0 as the action sign to end the program')

while True:
    s = input('Select an action(+,-,*,/,**):')
    if s == '0':
        break
    if s in ('+', '-', '*', '/', '**'):
        x = float(input('Enter the first number:'))
        y = float(input('Enter the second number:'))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '**':
            print("%.2f" % (x**y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print('You cant divide by 0')
    else:
        print('Invalid operation sign')
