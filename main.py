import numpy as np
import matplotlib.pyplot as plt

TEMP = np.zeros((6, 48))
for i in range(0,47):
    x=i-5
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

UST = np.zeros((6, 100))
for i in range(0,100):
    x=i
    UST[0, i] = x


    if x >= 0 and x <= 50:
        UstZimna = (50 - x) / (50 - 0)
    else:
        UstZimna = 0
    UST[1, i] = UstZimna

    if x >= 20 and x <= 60:
       UstSrednia = (x - 20) / (60 - 20)
    elif x >= 60 and x <= 80:
       UstSrednia = (80 - x) / (80 - 60)
    else:
       UstSrednia = 0
    UST[2,i] = UstSrednia

    if x >= 60 and x <= 100:
        UstWysoka = (x - 60) / (100 - 60)
    else:
        UstWysoka = 0
    UST[3, i] = UstWysoka
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

plt.plot(UST[0, :], UST[2, :], 'g')
plt.axis([0,100,0,1.1])

plt.plot(UST[0, :], UST[3, :], 'y')
plt.axis([0,100,0,1.1])

TempPokoju = 10+ 5

TempUstawiana = 20+5

Zmiana = TempUstawiana-TempPokoju

print(TEMP[1,Zmiana], TEMP[2,Zmiana], TEMP[3,Zmiana], TEMP[4,Zmiana])

#TEMP1= Zimno / TEMP2= Letnio / TEMP3 = Cieplo / TEMP4 = Goraco


#r1 IF Zmiana = Letnio  THEN Maly
#r2 IF Zmiana = Cieplo  THEN Sredni
#r3 IF Zmiana = Goraco  THEN Duzy



T1 = TEMP[1,Zmiana]
T2 = TEMP[2,Zmiana]
T3 = TEMP[3,Zmiana]
T4 = TEMP[4,Zmiana]

U1 = UST[1,Zmiana]
U2 = UST[2,Zmiana]
U3 = UST[3,Zmiana]



R1=min(T2,U1)
R2=min(T3,U2)
R3=min(T4,U3)




# print (US1,US2,US3,US4)
print (R1,R2,R3)





plt.show()
