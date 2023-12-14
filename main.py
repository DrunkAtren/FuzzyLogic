import numpy as np
import matplotlib.pyplot as plt

TEMP = np.zeros((6, 48))
for i in range(0,47):
    x=i-5
    TEMP[0, i] = x

    #temperatura zimno
    if x >= -5 and x <= 0:
       zimno = 1
    elif x >= 0 and x <= 10:
       zimno = (10-x)/(10-0)
    else:
       zimno = 0
    TEMP[1,i] = zimno

    # temperatura letnio
    if x>=0 and x<=10:
       letnio=(x-0)/(10-0)
    elif x>=10 and x<=20:
       letnio=(20-x)/(20-10)
    else:
       letnio=0
    TEMP[2,i] = letnio

    # temperatura cieplo
    if x >= 10 and x <= 20:
        cieplo = (x - 10) / (20 - 10)
    elif x >= 20 and x <= 30:
        cieplo = (30 - x) / (30 - 20)
    else:
        cieplo = 0
    TEMP[3, i] = cieplo

    # temperatura bardzo goraca
    if x >= 20 and x <= 30:
        goraco = (x - 20) / (30 - 20)
    elif x >= 30 and x <= 40:
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
plt.axis([-5,35,0,1.1])

plt.plot(TEMP[0, :], TEMP[2, :], 'green')
plt.axis([-5,35,0,1.1])

plt.plot(TEMP[0, :], TEMP[3, :], 'orange')
plt.axis([-5,35,0,1.1])

plt.plot(TEMP[0, :], TEMP[4, :], 'red')
plt.axis([-5,35,0,1.1])

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
