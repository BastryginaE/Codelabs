import matplotlib.pyplot as plt

class gen:
    def __init__(self, i, n, x):
        self.i=i
        self.n=n
        self.x=x

    def zap_mas(self):
        mas=[]
        for self.i in range(self.n):
            self.x += 10
            mas.append(self.x)
        self.i = 0
        self.x = 0
        return mas

    def zap_time(self):
        time=[]
        for self.i in range(self.n):
            self.x += 1
            time.append(self.x)
        self.i = 0
        self.x = 0
        return time

n = 25
i = 0
x = 0
gen_h=gen(i, n, x)
mas_w=gen_h.zap_mas()
time_w=gen_h.zap_time()
print(mas_w)
print(time_w)

w = int(input('Укажите размер окна:'))
window = []
i = 0

for i in range(w):
    x = 0
    window.append(x)

j=0
i=-n^2
v=0
h=0
summ=[]
suma=0
while i<=n:
    if j<=w-1 and v<=n-1:
        window[j]=mas_w[v]
        suma += window[j]
        calc=suma/w
        j+=1
        v+=1
        print(window)
        for h in range(1):
            summ.append(calc)

    else:
        j=0
    i+=1

print(summ)

fig, ax = plt.subplots()
ax.plot(time_w, summ, color="red", label="SMA")
ax.plot(time_w, mas_w, color="black", label="No SMA")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()

plt.show()
