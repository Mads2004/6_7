from typing import List, Tuple
# ---------- Utskrift av studieplan (Oppgave 4) ----------

def skriv_ut_studieplan(emnekoder: List[str],
                        semestre: List[str],
                        studiepoeng: List[int],
                        plan: List[List[int]]) -> None:
    """
    Skriv ut studieplanen med emner per semester, samt sum studiepoeng per semester.
    """
    if len(plan) != 6:
        print("Studieplanen skal ha nøyaktig 6 semestre (1–6).")
        return

    semnavn = {1: "Høst", 2: "Vår", 3: "Høst", 4: "Vår", 5: "Høst", 6: "Vår"}

    for i in range(6):
        sem_nummer = i + 1
        print(f"\nSemester {sem_nummer} ({semnavn[sem_nummer]}):")
        if not plan[i]:
            print("  (ingen emner)")
        total = 0
        for idx in plan[i]:
            try:
                kode = emnekoder[idx]
                sp = studiepoeng[idx]
                ses = "Høst" if semestre[idx].upper() == "H" else "Vår"
                print(f"  - {kode} ({sp} sp, {ses})")
                total += sp
            except IndexError:
                print(f"  ! Ugyldig emneindeks i plan: {idx} (finnes ikke i emnelistene)")
        print(f"  Sum: {total} studiepoeng")