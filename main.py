import numpy as np
import matplotlib.pyplot as plt
import time




TEMP = np.zeros((5, 48))
for i in range(0,47):
    x=i
    TEMP[0, i] = x

    #temperatura zimno
    if x >= 0 and x <= 5:
       zimno = 1
    elif x >= 5 and x <= 15:
       zimno = (15-x)/(15-5)
    else:
       zimno = 0
    TEMP[1,i] = zimno

    # temperatura letnio
    if x>=5 and x<=15:
       letnio=(x-5)/(15-5)
    elif x>=15 and x<=25:
       letnio=(25-x)/(25-15)
    else:
       letnio=0
    TEMP[2,i] = letnio

    # temperatura cieplo
    if x >= 15 and x <= 25:
        cieplo = (x - 15) / (25 - 15)
    elif x >= 25 and x <= 35:
        cieplo = (35 - x) / (35 - 25)
    else:
        cieplo = 0
    TEMP[3, i] = cieplo

    # temperatura bardzo goraca
    if x >= 25 and x <= 35:
        goraco = (x - 25) / (35 - 25)
    elif x >= 35 and x <= 40:
        goraco = 1
    else:
        goraco = 0
    TEMP[4, i] = goraco

UST = np.zeros((6, 110))
for i in range(0,110):
    x=i
    UST[0, i] = x

    if x == 0:
        UstWyl = 1
    else:
        UstWyl = 0
    UST[1, i] = UstWyl

    if x == 25:
        UstMaly = 1
    else:
        UstMaly = 0
    UST[2, i] = UstMaly

    if x == 50:
        UstSredni = 1
    else:
        UstSredni = 0
    UST[3, i] = UstSredni

    if x == 75:
        UstDuzy = 1
    else:
        UstDuzy = 0
    UST[4, i] = UstDuzy

    if x == 100:
        UstMax = 1
    else:
        UstMax = 0
    UST[5, i] = UstMax


plt.figure(1)

plt.xlabel('Temperatura [C]')
plt.ylabel('Wzrost')
plt.title('Zbiór rozmyty temperatury')

plt.plot(TEMP[0, :], TEMP[1, :], 'blue')
plt.axis([0,40,0,1.1])

plt.plot(TEMP[0, :], TEMP[2, :], 'green')
plt.axis([0,40,0,1.1])

plt.plot(TEMP[0, :], TEMP[3, :], 'orange')
plt.axis([0,40,0,1.1])

plt.plot(TEMP[0, :], TEMP[4, :], 'red')
plt.axis([0,40,0,1.1])

plt.figure(2)

plt.title('Ust')


plt.plot(UST[0, :], UST[1, :], 'b')
plt.axis([0,100,0,1.1])

plt.plot(UST[0, :], UST[2, :], 'b')
plt.axis([0,100,0,1.1])

plt.plot(UST[0, :], UST[3, :], 'b')
plt.axis([0,100,0,1.1])

plt.plot(UST[0, :], UST[4, :], 'b')
plt.axis([0,100,0,1.1])

plt.plot(UST[0, :], UST[5, :], 'b')
plt.axis([0,100,0,1.1])

TempZew = 15
TempPiec = 0
TempPokoju = TempZew + TempPiec
#Pokoj
TempUstawiana = 20


#TEMP1= Zimno / TEMP2= Letnio / TEMP3 = Cieplo / TEMP4 = Goraco

timeout = 5.0

def xyz():
    global Zmiana
    global TempPiec
    global TempPokoju
    global TempUstawiana

    TempPokoju = TempPokoju - 1 + TempPiec
    Zmiana = TempUstawiana - TempPokoju



    print("-----")
    print(TempPiec)

    print(TempPokoju)
    print(Zmiana)
    print(TEMP[1, Zmiana], TEMP[2, Zmiana], TEMP[3, Zmiana], TEMP[4, Zmiana])

    R1 = TEMP[1, Zmiana]
    R2 = TEMP[2, Zmiana]
    R3 = TEMP[3, Zmiana]
    R4 = TEMP[4, Zmiana]

    if Zmiana<0:
        TempPiec = 0
    elif R4 > 0:
        TempPiec = 5
    elif R3 > 0:
        TempPiec = 4
    elif R2 > 0:
        TempPiec = 3
    elif R1 > 0:
        TempPiec = 2
    time.sleep(5)

while True:
    xyz()

plt.show()
#r1 IF Zmiana = Zimno THEN Maly
#r2 IF Zmiana = Letnio  THEN Sredni
#r3 IF Zmiana = Cieplo  THEN Duzy
#r4 IF Zmiana = Goraco  THEN Max
#r5 IF Zmiana<0 THEN Wylacz