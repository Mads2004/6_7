# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 17:48:07 2025

@author: simen
"""

#emnekode
#semester
#studiepoeng
#studieplan

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

def oppgave1(emnekode, semester, studiepoeng):
    #emnekode = []
    #semester = []
    #studiepoeng = []
    
    print("=== Registrering av emner ===")
    print("Skriv 'stopp' som emnekode for å avslutte.\n")
    
    while True:
        kode = input("Skriv inn emnekode: ").upper()
    
        # Avslutt hvis brukeren skriver 'stopp'
        if kode == "STOPP":
            break
    
        # Sjekk om emnet finnes fra før
        if kode in emnekode:
            print(" Dette emnet finnes allerede. Prøv igjen.\n")
            continue
    
        sem = input("Hvilket semester undervises emnet (høst/vår): ").lower()
        poeng = int(input("Antall studiepoeng: "))
    
        # Legg til i listene
        emnekode.append(kode)
        semester.append(sem)
        studiepoeng.append(poeng)
    
        print(f" Emnet {kode} ({poeng} stp, {sem}) er lagt til.\n")
    
    # Etter brukeren avslutter, vis alle emner
    print("\n--- Registrerte emner ---")
    for i in range(len(emnekode)):
        print(f"{emnekode[i]} - {semester[i]} - {studiepoeng[i]} stp")
    
    print("\nProgrammet er avsluttet.")
    
    return emnekode, semester, studiepoeng

def oppgave2():
    
    emnekode = []
    emnesemester = []   # "høst" eller "vår"
    studiepoeng = []
    
    studieplan = [[], [], [], [], [], []]
    
    fortsetter = True
    while fortsetter:
        
        kode = input("Skriv inn emnekode: ")
        emnesem = input("Hvilket semester undervises emnet (høst/vår): ").lower()
        poeng = int(input("Antall studiepoeng: "))
        
        emnekode.append(kode)
        emnesemester.append(emnesem)
        studiepoeng.append(poeng)
        
        print(f"\nEmnet {kode} er lagt til med {poeng} studiepoeng i {emnesem}-semesteret.")
        
        semnr = int(input("\nHvilket semester (1-6) vil du legge emnet i: "))
        indeks = emnekode.index(kode)
        
        for s in studieplan:
            if indeks in s:
                print("Feil: Emnet finnes allerede i studieplanen.")
                continue
        
        if emnesemester[indeks] == "høst" and semnr not in [1, 3, 5]:
            print("Feil: Høstemne kan bare legges til i semester 1, 3 eller 5.")
            continue
        elif emnesemester[indeks] == "vår" and semnr not in [2, 4, 6]:
            print("Feil: Våremne kan bare legges til i semester 2, 4 eller 6.")
            continue
        
        total_poeng = sum(studiepoeng[i] for i in studieplan[semnr - 1])
        if total_poeng + studiepoeng[indeks] > 30:
            print("Feil: Ikke plass, semesteret har maks 30 studiepoeng.")
            continue
        
        # Alt ok – legg til
        studieplan[semnr - 1].append(indeks)
        print(f" {kode} er lagt til i semester {semnr}.")
        
        print("\n--- Studieplan ---")
        for i in range(6):
            if studieplan[i]:
                koder = [emnekode[j] for j in studieplan[i]]
                poengsum = sum(studiepoeng[j] for j in studieplan[i])
                print(f"Semester {i+1}: {koder} ({poengsum} stp)")
            else:
                print(f"Semester {i+1}: (ingen emner)")            
                
def oppgave3():
    print 

def oppgave4(emnekode, semester, studiepoeng):
    studieplan = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}

    for i in range(len(emnekode)):
        sem = semester[i]
        if sem in studieplan:
            studieplan[sem].append(i)

    print("STUDIEPLAN")
    print("-" * 40)

    for semnr in range(1, 7):
        if semnr in (1, 3, 5):
            sesong = "Høst"
        else:
            sesong = "Vår"

        print(f"Semester {semnr} ({sesong})")

        if len(studieplan[semnr]) == 0:
            print("  (ingen emner)")
        else:
            total = 0
            for idx in studieplan[semnr]:
                print(f"  - {emnekode[idx]} ({studiepoeng[idx]} sp)")
                total += studiepoeng[idx]
            print(f"  Totalt: {total} studiepoeng\n")

    return studieplan
    
def oppgave5(emnekode, semester, studiepoeng):
    studieplan = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    for i in range(len(emnekode)):
        sem = semester[i]
        if sem in studieplan:
            studieplan[sem].append(i)

    gyldig = True
    avvik = []


    for semnr in range(1, 7):
        total = 0
        for idx in studieplan[semnr]:
            total += studiepoeng[idx]

        if total != 30:
            gyldig = False
            avvik.append((semnr, total))


    if gyldig:
        print("Studieplanen er gyldig (alle semestre har 30 studiepoeng).")
    else:
        print("Studieplanen er IKKE gyldig. Følgende semestre avviker fra 30 studiepoeng:")
        for semnr, sp in avvik:
            sesong = "Høst" if semnr in (1, 3, 5) else "Vår"
            print(f"  - Semester {semnr} ({sesong}): {sp} studiepoeng")

    return gyldig, avvik

def oppgave7():
    try:
        with open ("studiestuff.txt", "r") as fil:
            skriv_ut= fil.read()
            print(skriv_ut)
    except FileNotFoundError:
        print("filen finnes ikke")
    
def valg_1():#good
    oppgave1()
def valg_2(): #good
    oppgave2()
def valg_3():
    oppgave3()
    print("v3")
def valg_4():
    oppgave4()
    print("v4")
def valg_5():
    oppgave5()
    print("v5")
def valg_6():
    #open
    print("v6")
def valg_7(): #good
    oppgave7()
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
menyvalg = int(input("Velg et alternativ (1-8): "))

funksjon = menyvalg_funksjoner.get(menyvalg)
if funksjon:
    funksjon()
else:
    print("Ugyldig valg. Prøv igjen.")