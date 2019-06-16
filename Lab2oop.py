class Squareroot:
    def __init__(self, a):
        self.a=a
    def count(self):
        Xn=1
        A=1
        while A > 0:
            x=1/2*(Xn+self.a/Xn)
            if x != Xn:
                Xn=x
            else:
                break
        return x
a=float(input('Insert a positive number:'))
if a < 0:
    print ('Error: /a/ must be more than 0')
    a = float(input('Insert a positive number:'))
calc=Squareroot(a)
print('squareroot={}' .format(calc.count()))