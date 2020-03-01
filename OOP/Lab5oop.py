import matplotlib.pyplot as plt
import io
import re
import requests

class spam:
    def __init__(self, info):
        self.info = info

    def find(self):
        auth = []
        f = open(r'E:\mbox.txt', "wb")
        ufr = requests.get("http://www.pythonlearn.com/code3/mbox.txt")
        f.write(ufr.content)
        f.close()
        with io.open('mbox.txt', encoding='utf-8') as file:
            for line in file:
                if 'From: ' in line:
                    ls = len(line)
                    i = 0
                    while i < ls:
                        ch = ''
                        le = line[i]
                        while 'a'<= le <= 'z' or le == '.' or le == '@':
                            ch += le
                            i += 1
                            if i < ls:
                                le = line[i] 
                            else:
                                break
                        i += 1
                        if ch != '':
                            auth.append(ch)
        author_pure = list(set(auth))
        lap = len(author_pure)
        i = 0
        while i < lap:
            if re.search('(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)', author_pure[i]):
                i += 1
            else:
                del author_pure[i]
                lap -= 1
                i += 1
        author_pure.sort()
        log = open('mbox.txt', 'r')
        lap = len(author_pure)
        i = 0
        log_line = log.readlines()
        line_ln = len(log_line)
        j = 0
        coef = []
        coeff_us = {}
        mail_us = {}
        coefec = []
        while j < lap:
            count = 0
            while i < line_ln:
                if 'From: ' + author_pure[j] in log_line[i]:
                    gti = i
                    count += 1
                    while gti < line_ln:
                        if 'X-DSPAM-Confidence: ' in log_line[gti]:
                           gt = 0
                           gl = log_line[gti]
                           eln = len(gl)
                           while gt < eln:
                               gt_num = ''
                               elg = log_line[gti]
                               while '0' <= elg[gt] <= '9' or elg[gt] == '.':
                                   gt_num += elg[gt]
                                   gt += 1
                                   if gt < eln:
                                       elg = log_line[gti]
                                   else:
                                       break
                               gt += 1
                               if gt_num != '':
                                   cf = float(gt_num)
                                   coef.append(cf)
                           break
                        else:
                            gti += 1
                    i += 1
                else:
                    i += 1
            cfqn = len(coef)
            if cfqn != 0:
                cfsum = 0
                for k in range(cfqn):
                    cfsum += coef[k]
                    cfavr = cfsum/cfqn
                    coefec.append(cfavr)
                    coeff_us.update({author_pure[j]: coefec[j]})
                    mail_us.update({author_pure[j]: count})
            j += 1
            i = 0
            coef.clear()
        return(coeff_us, mail_us, author_pure)

info = 0

res = spam(info)

coeff, mail, author = res.find()

fig, ax = plt.subplots()
plt.xticks(rotation = 'vertical')
ax.bar(mail.keys(), mail.values(), color = "green")

fig.set_figwidth(14)
fig.set_figheight(8)

ax.set_xlabel("x")
ax.set_ylabel("y")

plt.show()

i = 0
n = len(coeff)
for i in range(n):
    if coeff.get(auth[i]) > 0.95:
        print('Recommended for spam blocking: ', auth[i])


















