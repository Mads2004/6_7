# -*- coding: utf-8 -*-
def oppgave2(emnekode, semester, studiepoeng, studieplan):
    print("\n=== Legg til emne i studieplan ===")

    if not emnekode:
        print("Ingen emner er registrert ennå. Bruk alternativ 1 først.")
        return studieplan

    print("Registrerte emner:")
    for i in range(len(emnekode)):
        print(f"{i + 1}. {emnekode[i]} ({studiepoeng[i]} stp, {semester[i]})")

    valg = input("\nSkriv inn emnekoden du vil legge til i studieplanen: ").upper()

    if valg not in emnekode:
        print("Ugyldig emnekode. Emnet finnes ikke.")
        return studieplan

    # Velg semesterplassering
    try:
        semnr = int(input("Hvilket semester (1–6) skal emnet legges til i? "))
        if semnr < 1 or semnr > 6:
            print("Ugyldig semester. Må være mellom 1 og 6.")
            return studieplan
    except ValueError:
        print("Ugyldig input. Skriv et tall mellom 1 og 6.")
        return studieplan

    # Sjekk om emnet allerede er lagt til i det semesteret
    for emne, sem in studieplan:
        if emne == valg and sem == semnr:
            print(f"Emnet {valg} finnes allerede i semester {semnr}.")
            return studieplan

    # Legg til emnet med semester
    studieplan.append((valg, semnr))
    print(f"Emnet {valg} er lagt til i semester {semnr}.")

    return studieplan

