import numpy as np
import matplotlib.pyplot as plt

TEMPZEWN = np.zeros((6, 48))

for i in range(0,47):
    x=i-5
    TEMPZEWN[0, i] = x

    #temperatura bardzo zimno
    if x >= -5 and x <= 0:
       bzimno = 1
    elif x >= 0 and x <= 5:
       bzimno = (5-x)/(5-0)
    else:
       bzimno = 0
    TEMPZEWN[1,i] = bzimno

    # temperatura zimno
    if x>=0 and x<=5:
       zimno=(x-0)/(5-0)
    elif x>=5 and x<=10:
       zimno=1
    elif x>=10 and x<=15:
       zimno=(15-x)/(15-10)
    else:
       zimno=0
    TEMPZEWN[2,i] = zimno

    # temperatura umiarkowana
    if x >= 10 and x <= 12:
        umiarkowana = (x - 10) / (12 - 10)
    elif x >= 12 and x <= 17:
        umiarkowana = 1
    elif x >= 17 and x <= 20:
        umiarkowana = (20 - x) / (20 - 17)
    else:
        umiarkowana = 0
    TEMPZEWN[3, i] = umiarkowana

    # temperatura goraca
    if x >= 15 and x <= 20:
        goraco = (x - 15) / (20 - 15)
    elif x >= 20 and x <= 25:
        goraco = 1
    elif x >= 25 and x <= 30:
        goraco = (30 - x) / (30 - 25)
    else:
        goraco = 0
    TEMPZEWN[4, i] = goraco

    # temperatura bardzo goraca
    x = -5 + i
    if x >= 25 and x <= 30:
        bgoraco = (x - 25) / (30 - 25)
    elif x >= 30 and x <= 40:
        bgoraco = 1
    else:
        bgoraco = 0
    TEMPZEWN[5, i] = bgoraco

#---- graficzna prezentacja zbiorow temperatury
plt.figure(1)

plt.xlabel('Temperatura [C]')
plt.ylabel('Wzrost')
plt.title('Zbiór rozmyty temperatury')

plt.text(-4.7, 1.01, 'Bardzo zimno', fontsize = 7)
plt.plot(TEMPZEWN[0, :], TEMPZEWN[1, :], 'b')
plt.axis([-5,4,0,1.1])

plt.text(5, 1.01, 'Zimno', fontsize = 7)
plt.plot(TEMPZEWN[0,:],TEMPZEWN[2,:],'g')
plt.axis([-5,35,0,1.1])

plt.text(11.9, 1.01, 'Umiarkowanie', fontsize = 7)
plt.plot(TEMPZEWN[0, :], TEMPZEWN[3, :], 'y')
plt.axis([-5,35,0,1.1])

plt.text(20, 1.01, 'Goraco', fontsize = 7)
plt.plot(TEMPZEWN[0, :], TEMPZEWN[4, :], 'orange')
plt.axis([-5,35,0,1.1])

plt.text(29.4, 1.01, 'Bardzo goraco', fontsize = 7)
plt.plot(TEMPZEWN[0, :], TEMPZEWN[5, :], 'red')
plt.axis([-5,35,0,1.1])

#testowanie wartosci
value = 18
value_git = value + 5
print(TEMPZEWN[1,value_git],TEMPZEWN[2,value_git],TEMPZEWN[3,value_git],TEMPZEWN[4,value_git],TEMPZEWN[5,value_git])


plt.show()

