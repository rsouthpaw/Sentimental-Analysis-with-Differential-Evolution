#This file also contains various options for you to plot data for DE
#Use according to your need
#Last one is tested and works well
#Install the library befor use

m=''
with open('C:\Users\Saransh01\Desktop\Power\kk.txt', 'rb') as f:
    for line in f:
        if line.startswith(' "text":'):
            g=line.strip()
            g.replace('"text": "',' ')
            m=m+p
i=0
j=0
ff=[i][j]
for i in range(0,100)

m=[]
with open('C:\Users\Saransh01\Desktop\Power\kk.txt', 'rb') as f:
    for line in f:
        if line.startswith('  "friends_count": '):
            g=line.strip()
            h=g.replace('"friends_count": ','0')
            k=h.replace(',','0')
            b=int(k)
            b=b/10;
            m.append(b)

l=[]
with open('C:\Users\Saransh01\Desktop\Power\kk.txt', 'rb') as f:
    for line in f:
        if line.startswith('  "followers_count": '):
            g=line.strip()
            h=g.replace('"followers_count": ','0')
            k=h.replace(',','0')
            b=int(k)
            b=b/10;
            c=int(math.log(b,2))
            l.append(c) 

m=[]
with open('C:\Users\Saransh01\Desktop\Power\kk.txt', 'rb') as f:
    for line in f:
        if line.startswith('  "friends_count": '):
            g=line.strip()
            h=g.replace('"friends_count": ','0')
            k=h.replace(',','0')
            b=int(k)
            b=b/10
            if b < 2:
                c=0
            elif b >= 2:
                c=int(math.log(b,2))
            m.append(c)

import matplotlib.pyplot as plt
plt.plot(m,l,'ro')
plt.axis([0, max(m)+5, 0, max(l)+5])
plt.show()



#mail id: saranshmiglani@gmail.com