# -*- coding: utf-8 -*-
try:
    with open ("studiestuff.txt", "w") as fil:
        fil.write(f"{'Studieplan':<10}   {'Emner':>30}\n")
        fil.write("" "\n")
        for i, semesterliste in enumerate(studieplan+1):
         fil.write(f"Semester {i}| {semesterliste}")  
        
       


except FileNotFoundError:
    print("fant ikke flien")


