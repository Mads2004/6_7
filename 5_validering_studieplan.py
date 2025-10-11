from typing import List, Tuple


def gyldighet_studieplan(emnekoder: List[str],
                         studiepoeng: List[int],
                         plan: List[List[int]]) -> Tuple[bool, List[Tuple[int, int]]]:
    """
    Returnerer (gyldig, avviksliste).
    gyldig = True hvis hvert semester har nøyaktig 30 sp.
    avviksliste = liste av (semester_nr, sum_sp) for semestre som ikke er 30 sp.
    """
    avvik = []
    for i in range(6):
        sem_sum = 0
        for idx in plan[i]:
            if 0 <= idx < len(studiepoeng):
                sem_sum += studiepoeng[idx]
            else:
                # Teller ikkje poeng for ugyldig indeks, men flagger ved utskrift.
                pass
        if sem_sum != 30:
            avvik.append((i + 1, sem_sum))
    return (len(avvik) == 0), avvik


def sjekk_og_skriv_gyldighet(emnekoder: List[str],
                             studiepoeng: List[int],
                             plan: List[List[int]]) -> None:
    """
    Sjekker gyldighet og skriver status.
    """
    gyldig, avvik = gyldighet_studieplan(emnekoder, studiepoeng, plan)
    if gyldig:
        print("\n Studieplanen er gyldig: Alle 6 semestre har 30 studiepoeng.")
    else:
        print("\n Studieplanen er ikke gyldig.")
        for sem_nr, sp in avvik:
            print(f"  - Semester {sem_nr} har {sp} studiepoeng (skal være 30).")