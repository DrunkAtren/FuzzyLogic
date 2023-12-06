import numpy as np
import matplotlib.pyplot as plt

TEMP = np.zeros((6, 48))
for i in range(0,47):
    x=i-5
    TEMP[0, i] = x

    #temperatura bardzo zimno
    if x >= -5 and x <= 0:
       bzimno = 1
    elif x >= 0 and x <= 5:
       bzimno = (5-x)/(5-0)
    else:
       bzimno = 0
    TEMP[1,i] = bzimno

    # temperatura zimno
    if x>=0 and x<=5:
       zimno=(x-0)/(5-0)
    elif x>=5 and x<=10:
       zimno=1
    elif x>=10 and x<=15:
       zimno=(15-x)/(15-10)
    else:
       zimno=0
    TEMP[2,i] = zimno

    # temperatura umiarkowana
    if x >= 10 and x <= 13:
        umiarkowana = (x - 10) / (13 - 10)
    elif x >= 13 and x <= 17:
        umiarkowana = 1
    elif x >= 17 and x <= 20:
        umiarkowana = (20 - x) / (20 - 17)
    else:
        umiarkowana = 0
    TEMP[3, i] = umiarkowana

    # temperatura goraca
    if x >= 15 and x <= 20:
        goraco = (x - 15) / (20 - 15)
    elif x >= 20 and x <= 25:
        goraco = 1
    elif x >= 25 and x <= 30:
        goraco = (30 - x) / (30 - 25)
    else:
        goraco = 0
    TEMP[4, i] = goraco

    # temperatura bardzo goraca
    x = -5 + i
    if x >= 25 and x <= 30:
        bgoraco = (x - 25) / (30 - 25)
    elif x >= 30 and x <= 40:
        bgoraco = 1
    else:
        bgoraco = 0
    TEMP[5, i] = bgoraco

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


#---- graficzna prezentacja zbiorow temperatury
plt.figure(1)

plt.xlabel('Temperatura [C]')
plt.ylabel('Wzrost')
plt.title('Zbiór rozmyty temperatury')

plt.plot(TEMP[0, :], TEMP[1, :], 'b')
plt.axis([-5,4,0,1.1])

plt.plot(TEMP[0, :], TEMP[2, :], 'g')
plt.axis([-5,35,0,1.1])

plt.plot(TEMP[0, :], TEMP[3, :], 'y')
plt.axis([-5,35,0,1.1])

plt.plot(TEMP[0, :], TEMP[4, :], 'orange')
plt.axis([-5,35,0,1.1])

plt.plot(TEMP[0, :], TEMP[5, :], 'red')
plt.axis([-5,35,0,1.1])

plt.figure(2)

plt.xlabel('Temperatura [C]')
plt.ylabel('Wzrost')
plt.title('Zbiór rozmyty temperatury')


plt.plot(UST[0, :], UST[1, :], 'b')
plt.axis([-5,35,0,1.1])

plt.plot(UST[0, :], UST[2, :], 'g')
plt.axis([-5,35,0,1.1])

plt.plot(UST[0, :], UST[3, :], 'y')
plt.axis([-5,35,0,1.1])

#testowanie wartosci
TempZew = 0
TempPiec = 12

TempPokoju = 5+ 5

TempUstawiana = 19+5

print(TEMP[1,TempPokoju], TEMP[2,TempPokoju], TEMP[3,TempPokoju], TEMP[4,TempPokoju], TEMP[5,TempPokoju])

#TEMP1= Bardzo zimny / TEMP2= Zimno / TEMP3 = Umiarkowanie / TEMP 4 = Goraco / TEMP5 = Bardzo goraco


#Maly =[0.5,1,0.5,0,0]
#Sredni ={0,0.5,1.0,0.5,0}
#Duzy ={0,0,0,0.5,1.0}

#r1 IF TempPokoju = Bardzo zimny AND TempUstawiana = UstSrednia THEN Sredni
#r2 IF TempPokoju = Bardzo zimny AND TempUstawiana = UstWysoka THEN Duzy
#r3 IF TempPokoju = Zimny AND TempUstawiana = UstSrednia THEN Maly
#r4 IF TempPokoju = Zimny AND TempUstawiana = UstWysoka THEN Duzy
#r5 IF TempPokoju = Umiarkowana AND TempUstawiana = UstWysoka THEN Duzy

T1 = TEMP[1,TempPokoju]
T2 = TEMP[2,TempPokoju]
T3 = TEMP[3,TempPokoju]

U2 = UST[2,TempUstawiana]
U3 = UST[3,TempUstawiana]

R1=min(T1,U2)
R2=min(T1,U3)
R3=min(T2,U2)
R4=min(T2,U3)
R5=min(T3,U3)

a = UST[1,TempUstawiana]
b = UST[2,TempUstawiana]
c = UST[3,TempUstawiana]

Maly =[0.5,1,0.5,0,0]
Sredni = [0,0.5,1.0,0.5,0]
Duzy = [0,0,0,0.5,1.0]

print (a,b,c)
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

print(Maly)



#TEMP[1,TempPokoju] UST[2,TempUstawiana]
#TEMP[1,TempPokoju] UST[3,TempUstawiana]
#TEMP[2,TempPokoju] UST[2,TempUstawiana]
#TEMP[2,TempPokoju] UST[3,TempUstawiana]
#TEMP[3,TempPokoju] UST[3,TempUstawiana]

#UstZimna UstSrednia UstWysoka

plt.show()



#r1 IF TempPokoju = Bardzo zimny AND TempUstawiana = UstZimna THEN Wylacz
#r2 IF TempPokoju = Bardzo zimny AND TempUstawiana = UstSrednia THEN Sredni
#r3 IF TempPokoju = Bardzo zimny AND TempUstawiana = UstWysoka THEN Duzy

#r4 IF TempPokoju = Zimny AND TempUstawiana = UstZimna THEN Wylacz
#r5 IF TempPokoju = Zimny AND TempUstawiana = UstSrednia THEN Maly
#r6 IF TempPokoju = Zimny AND TempUstawiana = UstWysoka THEN Duzy

#r7 IF TempPokoju = Umiarkowana AND TempUstawiana = UstZimna THEN Wylacz
#r8 IF TempPokoju = Umiarkowana AND TempUstawiana = UstSrednia THEN Wylacz
#r9 IF TempPokoju = Umiarkowana AND TempUstawiana = UstWysoka THEN Duzy

#r10 IF TempPokoju = Goraco AND TempUstawiana = UstZimna THEN Wylacz
#r11 IF TempPokoju = Goraco AND TempUstawiana = UstSrednia THEN Wylacz
#r12 IF TempPokoju = Goraco AND TempUstawiana = UstWysoka THEN Wylacz

#r13 IF TempPokoju = BGoraco AND TempUstawiana = UstZimna THEN Wylacz
#r14 IF TempPokoju = BGoraco AND TempUstawiana = UstSrednia THEN Wylacz
#r15 IF TempPokoju = BGoraco AND TempUstawiana = UstWysoka THEN Wylacz