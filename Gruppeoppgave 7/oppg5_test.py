# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 15:53:38 2025

@author: simen
"""


def oppgave5():
    # Samme lister
    emnekode = ["DAT120", "ELE100", "YMF100", "ELE130", "ELE140", "YMF110", "KUK200", "ELE200", "ELE610", "ELE300", "SEX420"]
    semester = [1, 1, 1, 2, 2, 2, 3, 3, 4, 3, 4]
    studiepoeng = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,]

    # Lager studieplan slik som i oppg. 4
    studieplan = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    for i in range(len(emnekode)):
        sem = semester[i]
        studieplan[sem].append(i)

    # Sjekk om hvert semester har 30 studiepoeng
    gyldig = True
    avvik = []

    for semnr in range(1, 7):
        total = 0
        for idx in studieplan[semnr]:
            total += studiepoeng[idx]

        if total != 30:
            gyldig = False
            avvik.append((semnr, total))

    # Utskrift og returverdi
    if gyldig:
        print("Studieplanen er gyldig (alle semestre har 30 studiepoeng).")
    else:
        print("Studieplanen er IKKE gyldig. Følgende semestre har feil antall studiepoeng:")
        for semnr, sp in avvik:
            sesong = "Høst" if semnr in (1, 3, 5) else "Vår"
            print(f"  - Semester {semnr} ({sesong}): {sp} studiepoeng")

    return gyldig, avvik


# Testkjøring
if __name__ == "__main__":
    oppgave5()