import numpy as np
import matplotlib.pyplot as plt

bzimno1=np.zeros((2, 72))
for i in range(0,71):
     x=-5+i
     bzimno1[0,i]=x
     if x>=-5 and x<=0:
        bzimno=1
     elif x>=0 and x<=5:
        bzimno=(5-x)/(5-0)
     else:
        bzimno=0
     bzimno1[1,i] = bzimno

zimno1=np.zeros((2,72))
for i in range(0,71):
     x=-5+i
     zimno1[0,i]=x
     if x>=0 and x<=5:
        zimno=(x-0)/(5-0)
     elif x>=5 and x<=10:
        zimno=1
     elif x>=10 and x<=15:
        zimno=(15-x)/(15-10)
     else:
        zimno=0
     zimno1[1,i] = zimno

umiarkowana1 = np.zeros((2, 72))
for i in range(0, 71):
     x = -5 + i
     umiarkowana1[0, i] = x
     if x >= 10 and x <= 12:
         umiarkowana = (x - 10) / (12 - 10)
     elif x >= 12 and x <= 17:
         umiarkowana = 1
     elif x >= 17 and x <= 20:
         umiarkowana = (20 - x) / (20 - 17)
     else:
         umiarkowana = 0
     umiarkowana1[1, i] = umiarkowana

goraco1 = np.zeros((2, 72))
for i in range(0, 71):
    x = -5 + i
    goraco1[0, i] = x
    if x >= 15 and x <= 20:
        goraco = (x - 15) / (20 - 15)
    elif x >= 20 and x <= 25:
        goraco = 1
    elif x >= 25 and x <= 30:
        goraco = (30 - x) / (30 - 25)
    else:
        goraco = 0
    goraco1[1, i] = goraco

bgoraco1 = np.zeros((2, 72))
for i in range(0, 71):
    x = -5 + i
    bgoraco1[0, i] = x
    if x >= 25 and x <= 30:
        bgoraco = (x - 25) / (30 - 25)
    elif x >=30  and x <= 35:
        bgoraco = 1
    else:
        bgoraco = 0
    bgoraco1[1, i] = bgoraco

#---- graficzna prezentacja zbiorow temperatury
plt.figure(1)
plt.subplot(1, 1, 1)
plt.text(0, 10, 'Bardzo zimno', fontsize = 12)
plt.plot(bzimno1[0, :], bzimno1[1, :], 'b')
plt.axis([-5,35,0,1.2])
plt.xlabel('Temperatura [C]')
plt.ylabel('Wzrost')
plt.title('Zbiór rozmyty temperatury')

plt.subplot(1, 1, 1)
plt.plot(zimno1[0,:],zimno1[1,:],'g')
plt.axis([-5,35,0,1.2])

plt.subplot(1, 1, 1)
plt.plot(umiarkowana1[0, :], umiarkowana1[1, :], 'y')
plt.axis([-5,35,0,1.2])

plt.subplot(1, 1, 1)
plt.plot(goraco1[0, :], goraco1[1, :], 'r')
plt.axis([-5,35,0,1.2])

plt.subplot(1, 1, 1)
plt.plot(bgoraco1[0, :], bgoraco1[1, :], 'black')
plt.axis([-5,35,0,1.2])

plt.show()

