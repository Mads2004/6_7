# -*- coding: utf-8 -*-
"""
Created on Mon Oct 13 16:03:08 2025

@author: Mads
"""
def oppgave2(emnekode, semester, studiepoeng, studieplan):
    print(" Legg til emne i studieplan ")

    if not emnekode:
        print("Ingen emner er registrert ennå. Bruk alternativ 1 først.")
        return studieplan

    print("Registrerte emner:")
    for i in range(len(emnekode)):
        print(f"{i + 1}. {emnekode[i]} ({studiepoeng[i]} stp, {semester[i]})\n")

    print("Skriv 'stopp' som emnekode for å avslutte.")
    
    while len(studieplan) < 6:
        studieplan.append([])
   
    while True:
       print("Registrerte emner:")
       for i in range(len(emnekode)):
           print(f"{i + 1}. {emnekode[i]} ({studiepoeng[i]} stp, {semester[i]})\n")
        
       valg = input("Skriv inn emnekoden du vil legge til i studieplanen: ").upper()
   
       if valg == "STOPP":
           break
   
       if valg not in emnekode:
           print("Ugyldig emnekode. Emnet finnes ikke.")
           continue

       index = emnekode.index(valg)
       sesong = semester[index]

       if sesong == "høst":
           semnr = int(input("Hvilket semester (1,3,5) skal emnet legges til i? ")) 
       elif sesong == "vår":
           semnr = int(input("Hvilket semester (2,4,6) skal emnet legges til i? "))
       else:
           print("Ikke gyldig semester")
           continue

       if semnr < 1 or semnr > 6:
           print("Ugyldig semester. Må være mellom 1 og 6.")
           continue

       if valg in studieplan[semnr - 1]:
           print(f"Emnet {valg} finnes allerede i semester {semnr}.")
           continue

       studieplan[semnr - 1].append(valg)

       print(f"Emnet {valg} er lagt til i semester {semnr}.")
       print("Oppdatert studieplan:")
       for i, semesterliste in enumerate(studieplan, start=1):
           print(f"Semester {i}: {semesterliste}")
           
    print("\nSender bruker tilbake til meny.")
    return studieplan

