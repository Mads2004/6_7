# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 17:22:09 2025

<<<<<<< Updated upstream
@author: simen
=======
@author: Mads
>>>>>>> Stashed changes
"""
emnekode = []
semester = []
studiepoeng = []

def oppgave1(emnekode, semester, studiepoeng):
<<<<<<< Updated upstream
    #emnekode = []
    #semester = []
    #studiepoeng = []
    
    print("=== Registrering av emner ===")
=======
    
    print("Registrering av emner")
>>>>>>> Stashed changes
    print("Skriv 'stopp' som emnekode for å avslutte.\n")
    
    while True:
        kode = input("Skriv inn emnekode: ").upper()
    
<<<<<<< Updated upstream
        # Avslutt hvis brukeren skriver 'stopp'
        if kode == "STOPP":
            break
    
        # Sjekk om emnet finnes fra før
=======
        if kode == "STOPP":
            break
    
>>>>>>> Stashed changes
        if kode in emnekode:
            print(" Dette emnet finnes allerede. Prøv igjen.\n")
            continue
    
        sem = input("Hvilket semester undervises emnet (høst/vår): ").lower()
        poeng = int(input("Antall studiepoeng: "))
    
<<<<<<< Updated upstream
        # Legg til i listene
=======
>>>>>>> Stashed changes
        emnekode.append(kode)
        semester.append(sem)
        studiepoeng.append(poeng)
    
        print(f" Emnet {kode} ({poeng} stp, {sem}) er lagt til.\n")
    
<<<<<<< Updated upstream
    # Etter brukeren avslutter, vis alle emner
=======
>>>>>>> Stashed changes
    print("\n--- Registrerte emner ---")
    for i in range(len(emnekode)):
        print(f"{emnekode[i]} - {semester[i]} - {studiepoeng[i]} stp")
    
<<<<<<< Updated upstream
    print("\nProgrammet er avsluttet.")
=======
    print("\nSender bruker tilbake til meny.")
>>>>>>> Stashed changes
    return emnekode, semester, studiepoeng
