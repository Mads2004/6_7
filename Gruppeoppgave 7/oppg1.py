# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 17:22:09 2025

@author: Mads
"""
emnekode = []
semester = []
studiepoeng = []

def oppgave1(emnekode, semester, studiepoeng):
    
    print("Registrering av emner")
    print("Skriv 'stopp' som emnekode for å avslutte.\n")
    
    while True:
        kode = input("Skriv inn emnekode: ").upper()
    
        if kode == "STOPP":
            break
    
        if kode in emnekode:
            print(" Dette emnet finnes allerede. Prøv igjen.\n")
            continue
    
        sem = input("Hvilket semester undervises emnet (høst/vår): ").lower()
        poeng = int(input("Antall studiepoeng: "))
    
        emnekode.append(kode)
        semester.append(sem)
        studiepoeng.append(poeng)
    
        print(f" Emnet {kode} ({poeng} stp, {sem}) er lagt til.\n")
    
    print("\n--- Registrerte emner ---")
    for i in range(len(emnekode)):
        print(f"{emnekode[i]} - {semester[i]} - {studiepoeng[i]} stp")
    
    print("\nSender bruker tilbake til meny.")
    return emnekode, semester, studiepoeng
