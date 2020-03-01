class Calculator:
    def __init__(self, a,b,x):
        if x == '+':
            result_c = a + b
            print(('Equals to {}'.format(result_c)))
        elif x == '-':
            result_c = a - b
            print(('Equals to {}'.format(result_c)))
        elif x == '*':
            result_c = a * b
            print(('Equals to {}'.format(result_c)))
        elif x == '/':
            try:
                result_c = a / b
                print(('Equals to {}'.format(result_c)))
            except(ZeroDivisionError):
              print(('You cannot use 0. Use another number'))

c = 'Next'
while c=='Next':
    a=float(input('Insert a:'))
    b=float(input('Insert b:'))
    x=str(input('Insert the sign:'))
    Calculator(a,b,x)

    c=str(input('Insert Next to continue or Stop to cut off: '))