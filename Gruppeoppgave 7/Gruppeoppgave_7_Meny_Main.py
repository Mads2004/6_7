# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 15:41:23 2025

@author: Simen,Ole,Mads,Jan Ståle
"""
from oppg1 import oppgave1
from oppg2 import oppgave2
from oppg4 import oppgave4
from oppg5 import oppgave5 

emnekode = []
semester = []
studiepoeng = []
studieplan = []

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
                
def oppgave3():
    print(emnekode)
    
def oppgave7():
    try:
        with open ("studiestuff.txt", "r") as fil:
            skriv_ut= fil.read()
            print(skriv_ut)
    except FileNotFoundError:
        print("filen finnes ikke")
    
def valg_1():#Good
    global emnekode,semester, studiepoeng
    emnekode, semester, studiepoeng = oppgave1(emnekode, semester, studiepoeng)
    velger()
def valg_2(): #good
    global studieplan
    studieplan = oppgave2(emnekode, semester, studiepoeng, studieplan)
    velger()
def valg_3(): #Good
    oppgave3()
    velger()
def valg_4():
    oppgave4()
    velger()
def valg_5():
    oppgave5()
    velger()
def valg_6():
    #open
    print("v6")
    velger()
def valg_7(): #Good
    oppgave7()
    velger()
def valg_8():#good
    print("Avslutter")

# Ordbok som kobler menyvalg til funksjoner
menyvalg_funksjoner = {
    1: valg_1,
    2: valg_2,
    3: valg_3,
    4: valg_4,
    5: valg_5,
    6: valg_6,
    7: valg_7,
    8: valg_8
}

# Eksempel på bruk
def velger():
    print(menytekst)
    menyvalg = int(input("Velg et alternativ (1-8): "))
    
    funksjon = menyvalg_funksjoner.get(menyvalg)
    if funksjon:
        funksjon()
    else:
        print("Ugyldig valg. Prøv igjen.")

velger()

