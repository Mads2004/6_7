# -*- coding: utf-8 -*-
try:
    with open ("studiestuff.txt", "r") as fil:
        skriv_ut= fil.read()
        print(skriv_ut)
except FileNotFoundError:
    print("filen finnes ikke")
