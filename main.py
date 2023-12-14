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

UST = np.zeros((6, 48))
for i in range(0,47):
    x=i-5
    UST[0, i] = x


    if x >= -5 and x <= 0:
        UstZimna = 1
    elif x >= 0 and x <= 10:
        UstZimna = (10 - x) / (10 - 0)
    else:
        UstZimna = 0
    UST[1, i] = UstZimna

    if x >= 0 and x <= 15:
       UstSrednia = (x - 0) / (15 - 0)
    elif x >= 15 and x <= 30:
       UstSrednia = (30 - x) / (30 - 15)
    else:
       UstSrednia = 0
    UST[2,i] = UstSrednia

    if x >= 20 and x <= 30:
        UstWysoka = (x - 20) / (30 - 20)
    elif x >= 30 and x <=35:
        UstWysoka = 1
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



TempPokoju = 10+ 5

TempUstawiana = 20+5

Zmiana = TempUstawiana-TempPokoju

print(TEMP[1,TempPokoju], TEMP[2,TempPokoju], TEMP[3,TempPokoju], TEMP[4,TempPokoju])

#TEMP1= Zimny / TEMP2= Letnio / TEMP3 = Cieplo / TEMP4 = Goraco


#r1 IF TempPokoju = Zimny AND Zmiana = Zimny THEN Zero
#r2 IF TempPokoju = Zimny AND Zmiana = UstMaly THEN Maly
#r3 IF TempPokoju = Zimny AND Zmiana = UstSrednia THEN Sredni
#r4 IF TempPokoju = Zimny AND Zmiana = UstDuzy THEN Duzy
#r5 IF TempPokoju = Zimny AND Zmiana = UstMax THEN Max

#r6 IF TempPokoju = Letnio AND Zmiana = UstZimna THEN Zero
#r7 IF TempPokoju = Letnio AND Zmiana = UstMaly THEN Zero
#r8 IF TempPokoju = Letnio AND Zmiana = UstSrednia THEN Zero
#r9 IF TempPokoju = Letnio AND Zmiana = UstDuzy THEN Duzy
#r10 IF TempPokoju = Letnio AND Zmiana = UstMax THEN Max

#r11 IF TempPokoju = Cieplo AND Zmiana = UstZimna THEN Zero
#r12 IF TempPokoju = Cieplo AND Zmiana = UstMaly THEN Zero
#r13 IF TempPokoju = Cieplo AND Zmiana = UstSrednia THEN Zero
#r14 IF TempPokoju = Cieplo AND Zmiana = UstDuzy THEN Zero
#r15 IF TempPokoju = Cieplo AND Zmiana = UstMax THEN Max

#r16 IF TempPokoju = Goraco AND Zmiana = UstZimna THEN Zero
#r17 IF TempPokoju = Goraco AND Zmiana = UstMaly THEN Zero
#r18 IF TempPokoju = Goraco AND Zmiana = UstSrednia THEN Zero
#r19 IF TempPokoju = Goraco AND Zmiana = UstDuzy THEN Zero
#r20 IF TempPokoju = Goraco AND Zmiana = UstMax THEN Max


T1 = TEMP[1,Zmiana]
T2 = TEMP[2,Zmiana]
T3 = TEMP[3,Zmiana]
T4 = TEMP[4,Zmiana]


U2 = WYJ[2,Zmiana]
U3 = WYJ[3,Zmiana]

R1=min(T1,U2)
R2=min(T1,U3)
R3=min(T2,U2)
R4=min(T2,U3)
R5=min(T3,U3)

R6=min(T1,U2)
R7=min(T1,U3)
R8=min(T2,U2)
R9=min(T2,U3)
R10=min(T3,U3)

R11=min(T1,U2)
R12=min(T1,U3)
R13=min(T2,U2)
R14=min(T2,U3)
R15=min(T3,U3)

R16=min(T1,U2)
R17=min(T1,U3)
R18=min(T2,U2)
R19=min(T2,U3)
R20=min(T3,U3)

# US1 = WYJ[1,TempUstawiana]
# US2 = WYJ[2,TempUstawiana]
# US3 = WYJ[3,TempUstawiana]
# US4 = WYJ[4,TempUstawiana]
# US5 = WYJ[5,TempUstawiana]


Zero =[1,0,0,0,0]
Maly =[0,1,0,0,0]
Sredni =[0,0,1,0,0]
Duzy =[0,0,0,1,0]
Max =[0,0,0,0,1]

# print (US1,US2,US3,US4)
print (R1,R2,R3,R4,R5)
if R3!=0:
    Maly =[min(0.5,R3),min(1,R3),min(0.5,R3),min(0,R3),min(0,R3),min(0,R3)]

if R1!=0:
    Sredni = [min(0,R1),min(0.5,R1),min(1,R1),min(0.5,R1),min(0,R1),min(0,R1)]

if  R2!=0:
    Duzy = [min(0, R2), min(0, R2), min(0, R2), min(0.5, R2), min(1, R2)]
elif R4!=0:
    Duzy = [min(0, R4), min(0, R4), min(0, R4), min(0.5, R4), min(1, R4)]
elif R5!=0:
    Duzy = [min(0, R5), min(0, R5), min(0, R5), min(0.5, R5), min(1, R5)]




plt.show()
