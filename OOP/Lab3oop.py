import argparse


class cl_parser:
    def __init__(self, poly):
        self.poly = poly

    def count (self):
        arpoly=len(self.poly)
        intlis = []
        i = 0
        while i < arpoly:
            num = ''
            find_num=self.poly[i]
            while '0'<=find_num<='9':
                num+=find_num
                i+=1
                if i<arpoly:
                    find_num=self.poly[i]
                else:
                    break
            i+=1
            if num !='':
                intlis.append(int(num))
        num_lis = len(intlis)

        j=0
        a=0
        while j<num_lis:
            x = 1/intlis[j]*3
            a+=x
            j+=1
        return a

parser = argparse.ArgumentParser(description='Poly')
parser.add_argument ('--poly', type=str, dest='poly')


args=parser.parse_args()

p=cl_parser(args.poly)
print(p.count())



