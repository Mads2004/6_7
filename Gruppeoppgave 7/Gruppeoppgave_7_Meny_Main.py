# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 15:41:23 2025

@author: Simen,Ole,Mads,Jan Ståle
"""
from oppg1 import oppgave1
from oppg2 import oppgave2
<<<<<<< Updated upstream
from oppg4 import oppgave4
=======
>>>>>>> Stashed changes
from oppg5 import oppgave5 

emnekode = []
semester = []
studiepoeng = []
studieplan = []

menytekst = """
<<<<<<< Updated upstream
=======
:::::::::::::::::::::
>>>>>>> Stashed changes
1. Lag et nytt emne
2. Legg til et emne i studieplanen
3. Liste over registrerte emner
4. Skriv ut studieplan med semesteroversikt
5. Kontroller gyldighet på studieplan
6. Lagre studieplan og emner til fil
7. Les inn studieplan og emner fra fil
8. Avslutt programm
<<<<<<< Updated upstream
"""
                
def oppgave3():
    print(emnekode)
    
=======
:::::::::::::::::::::
"""
                
def oppgave3():
    print("\nListe over registrerte emner:")
    for i in enumerate(emnekode,start=1):
        print(f"{i}\n")

def oppgave4():
    print(" ===Semesteroversikt=== ")
    for i, semesterliste in enumerate(studieplan, start=1):
        print(f"Semester {i}: {semesterliste}")

def oppgave6():
    try:
        with open ("studiestuff.txt", "w") as fil:
            fil.write(f"{'Studieplan':<10}   {'Emner':>5}\n")
            fil.write("" "\n")
            for i, semesterliste in enumerate(studieplan, start=1):
             fil.write(f"Semester {i}| {semesterliste}\n")         
    except FileNotFoundError:
        print("Filnavn ikke riktig")

>>>>>>> Stashed changes
def oppgave7():
    try:
        with open ("studiestuff.txt", "r") as fil:
            skriv_ut= fil.read()
            print(skriv_ut)
    except FileNotFoundError:
        print("filen finnes ikke")
<<<<<<< Updated upstream
    
def valg_1():#Good
    global emnekode,semester, studiepoeng
    emnekode, semester, studiepoeng = oppgave1(emnekode, semester, studiepoeng)
    velger()
def valg_2(): #good
    global studieplan
    studieplan = oppgave2(emnekode, semester, studiepoeng, studieplan)
    velger()
def valg_3(): #Good
=======

def oppgave8():
    print("Avslutter")

def valg_1():
    global emnekode,semester, studiepoeng
    emnekode, semester, studiepoeng = oppgave1(emnekode, semester, studiepoeng)
    velger()
def valg_2(): 
    global studieplan
    studieplan = oppgave2(emnekode, semester, studiepoeng, studieplan)
    velger()
def valg_3(): 
>>>>>>> Stashed changes
    oppgave3()
    velger()
def valg_4():
    oppgave4()
    velger()
<<<<<<< Updated upstream
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
=======
def valg_5(): 
    oppgave5(studieplan,studiepoeng,emnekode)
    velger()
def valg_6(): 
    oppgave6()
    velger()
def valg_7(): 
    oppgave7()
    velger()
def valg_8():
    oppgave8()

>>>>>>> Stashed changes
menyvalg_funksjoner = {
    1: valg_1,
    2: valg_2,
    3: valg_3,
    4: valg_4,
    5: valg_5,
    6: valg_6,
    7: valg_7,
    8: valg_8
<<<<<<< Updated upstream
}

# Eksempel på bruk
def velger():
    print(menytekst)
    menyvalg = int(input("Velg et alternativ (1-8): "))
    
=======
                      }

def velger():
    print(menytekst)
    menyvalg = int(input("Velg et alternativ (1-8):")) 
>>>>>>> Stashed changes
    funksjon = menyvalg_funksjoner.get(menyvalg)
    if funksjon:
        funksjon()
    else:
        print("Ugyldig valg. Prøv igjen.")

velger()

