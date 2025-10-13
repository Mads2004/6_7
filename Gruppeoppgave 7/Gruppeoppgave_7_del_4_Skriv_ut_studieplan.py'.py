# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 15:51:34 2025

@author: simen
"""

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

