import matplotlib.pyplot as plt

class stat:
    def __init__(self, i, n, x):
        self.i=i
        self.n=n
        self.x=x

    def rate(self):
        rate = []
        for self.i in range(self.n):
            self.x += 10
            rate.append(self.x)
        self.i = 0
        self.x = 0
        return rate

    def span(self):
        span = []
        for self.i in range(self.n):
            self.x += 1
            span.append(self.x)
        self.i = 0
        self.x = 0
        return span

n = 25
i = 0
x = 0
stat_h = stat(i, n, x)
rate_w = stat_h.rate()
span_w = stat_h.span()
print(rate_w)
print(span_w)

w_size = int(input('Input size of the window: '))
win = []
i = 0

for i in range(w_size):
    x = 0
    win.append(x)

j = 0
i = -n^2
a = 0
b = 0
sma_val = []
summ = 0
while i <= n:
    if j <= w_size-1 and a <= n-1:
        win[j] = rate_w[a]
        summ += win[j]
        sma_calc = summ/w_size
        j +=1
        a +=1
        print(win)
        for b in range(1):
            sma_val.append(sma_calc)
    else:
        j = 0
    i += 1

print(sma_val)

fig, ax = plt.subplots()
ax.plot(span_w, sma_val, color="green", label="SMA")
ax.plot(span_w, rate_w, color="blue", label="Initial_data")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()

plt.show()