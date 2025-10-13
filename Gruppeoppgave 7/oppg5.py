# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 15:55:17 2025

@author: simen
"""

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