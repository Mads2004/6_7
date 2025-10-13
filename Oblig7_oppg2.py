# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 17:04:32 2025

@author: madsj
"""

# --- Oppgave 2: Legg til emne i studieplanen ---

# Disse listene bør allerede inneholde data fra oppgave 1.
emnekode = []
semester = []
studiepoeng = []

# Seks semestre (1–6)
studieplan = [[], [], [], [], [], []]

print("=== Legg til emner i studieplanen ===")
print("Skriv 'stopp' som emnekode for å avslutte.\n")

while True:
    kode = input("Skriv inn emnekode du vil legge til i studieplanen: ").upper()
    if kode == "STOPP":
        break

    # Sjekk at emnet finnes
    if kode not in emnekode:
        print(" Emnet finnes ikke i emnelisten.\n")
        continue

    indeks = emnekode.index(kode)

    # Sjekk om emnet allerede er i studieplanen
    finnes = any(indeks in sem for sem in studieplan)
    if finnes:
        print(" Dette emnet er allerede i studieplanen.\n")
        continue

    semnr = int(input("Hvilket semester (1–6) vil du legge emnet i: "))

    # Sjekk gyldig semester
    if semnr < 1 or semnr > 6:
        print(" Ugyldig semester. Må være mellom 1 og 6.\n")
        continue

    # Sjekk at semesteret passer (høst/vår)
    if semester[indeks] == "høst" and semnr not in [1, 3, 5]:
        print(" Feil: Høstemne kan bare legges til i semester 1, 3 eller 5.\n")
        continue
    elif semester[indeks] == "vår" and semnr not in [2, 4, 6]:
        print(" Feil: Våremne kan bare legges til i semester 2, 4 eller 6.\n")
        continue

    # Sjekk poenggrense
    total_poeng = sum(studiepoeng[i] for i in studieplan[semnr - 1])
    if total_poeng + studiepoeng[indeks] > 30:
        print(" Ikke plass. Maks 30 studiepoeng i et semester.\n")
        continue

    # Alt ok → legg til
    studieplan[semnr - 1].append(indeks)
    print(f"✅ {kode} er lagt til i semester {semnr}.\n")

# Etterpå: skriv ut planen
print("\n--- Studieplan ---")
for i in range(6):
    if studieplan[i]:
        koder = [emnekode[j] for j in studieplan[i]]
        poengsum = sum(studiepoeng[j] for j in studieplan[i])
        print(f"Semester {i+1}: {koder} ({poengsum} stp)")
    else:
        print(f"Semester {i+1}: (ingen emner)")

print("\nProgrammet er avsluttet.")
