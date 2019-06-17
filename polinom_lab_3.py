import argparse
class Polinomial:
    def __init__(self, List):
        self.List=List
    def count (self):
        c=3
        length = len(self.List)
        format_List=[]
        a=0
        while a < length:
            blank_num=''
            index=self.List[a]
            while '0' <=index<='9':
                blank_num+=index
                a+=1
                if a<length:
                    a=self.List[a]
                else:
                    break
            a+=1
            if blank_num != '':
                format_List.append(int(blank_num))
        length2=len(format_List)
        cycle=0
        sum=0
        while cycle<length2:
            x=1/format_List[cycle]*c
            sum+=x
            cycle+=1
        return sum
parser=argparse.ArgumentParser(description='Polinomial')
parser.add_argument('--poly',action='store', dest='List',type=str)
args=parser.parse_args()
Poly=Polinomial(args.List)
print(Poly.count())
