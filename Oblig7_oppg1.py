# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 15:20:37 2025

@author: madsj
"""

emnekode = []
semester = []   # "høst" eller "vår"
studiepoeng = []

studieplan = [[], [], [], [], [], []]

kode = input("Skriv inn emnekode: ")
semester = input("Hvilket semester undervises emnet (høst/vår): ").lower()
poeng = int(input("Antall studiepoeng: "))

emnekode.append(kode)
semester.append(semester)
studiepoeng.append(poeng)

print(f"\nEmnet {kode} er lagt til med {poeng} studiepoeng i {semester}-semesteret.")

semnr = int(input("\nHvilket semester (1-6) vil du legge emnet i: "))
indeks = emnekode.index(kode)

for s in studieplan:
    if indeks in s:
        print("Feil: Emnet finnes allerede i studieplanen.")
        quit()

if semester[indeks] == "høst" and semnr not in [1, 3, 5]:
    print("Feil: Høstemne kan bare legges til i semester 1, 3 eller 5.")
    quit()
elif semester[indeks] == "vår" and semnr not in [2, 4, 6]:
    print("Feil: Våremne kan bare legges til i semester 2, 4 eller 6.")
    quit()

total_poeng = sum(studiepoeng[i] for i in studieplan[semnr - 1])
if total_poeng + studiepoeng[indeks] > 30:
    print("Feil: Ikke plass, semesteret har maks 30 studiepoeng.")
    quit()

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
