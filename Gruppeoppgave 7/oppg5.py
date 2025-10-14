# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 15:55:17 2025

@author: Jan Ståle
"""
  
def oppgave5(studieplan, studiepoeng, emnekode):
    gyldig = True
    avvik = []

    for semnr in range(1, 7):
        total = 0
        for emne in studieplan[semnr - 1]:
            if emne in emnekode:
                index = emnekode.index(emne)
                total += studiepoeng[index]
            else:
                print(f"Advarsel: Emnekode '{emne}' finnes ikke i listen over registrerte emner.")

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
