# -*- coding: utf-8 -*-
"""
Created on Sat Oct  4 18:20:31 2025

@author: simen
"""

menytekst = """
1. Lag et nytt emne
2. Legg til et emne i studieplanen
3. Liste over registrerte emner
4. Skriv ut studieplan med semesteroversikt
5. Kontroller gyldighet på studieplan
6. Lagre studieplan og emner til fil
7. Les inn studieplan og emner fra fil
8. Avslutt programm
"""

print(menytekst)
menyvalg = int(input("Velg en funksjon (1-8): "))

def valg_1():
    #open
    print("v1")
def valg_2():
    #open
    print("v2")
def valg_3():
    #print(liste(emnekode))
    print("v3")
def valg_4():
    #open
    print("v4")
def valg_5():
    #open
    print("v5")
def valg_6():
    #open
    print("v6")
def valg_7():
    #open
    print("v7")
def valg_8():
    print("Avslutter")
     
 
        
if menyvalg == 1:
   valg_1() 
elif menyvalg == 2:
    valg_2()
elif menyvalg == 3:
    valg_3()    
elif menyvalg == 4:
    valg_4()
elif menyvalg == 5:
    valg_5()
elif menyvalg == 6:
    valg_6()
elif menyvalg == 7:
    valg_7()
elif menyvalg == 8:
    valg_8()
else:
    print("Error")

#%%
while True:
    avslutter = print("Er du sikker på at du vil avslutte? (Ja/Nei):")
    if avslutter == "ja":
        print("3..2..1..")
        print("Avslutter.")
        break
    elif avslutter == "nei":
        print("menytekst.")
        break
    else:
        print("Ugyldig svar. Vennligst skriv 'ja' eller 'nei'.")
#%%

while True:
    avslutter = print("Er du sikker på at du vil avslutte? (Ja/Nei):")
    if avslutter == "ja":
        print("Avslutter.")
        break
    elif avslutter == "nei":
        print("menytekst.")
        break
    else:
        print("Ugyldig svar. Vennligst skriv 'ja' eller 'nei'.")
