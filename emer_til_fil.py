# -*- coding: utf-8 -*-
from itertools import zip_longest


try:
    with open ("studiestuff.txt", "w") as fil:
        fil.write(f"{'Studieplan':<10} | {'Emner':>10}\n")
        fil.write("" "\n")
        
        for emne, studie in zip_longest(emnekode, semester, fillvalue="."):
           fil.write(f"{studie:<10} | {emne:>10}\n")


except FileNotFoundError:
    print("fant ikke flien")


