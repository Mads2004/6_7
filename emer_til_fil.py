# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 21:01:20 2025

@author: Olli
"""

emner=["matte", "norsk", "engelsk", "naturfag", "historie", "gym"]

try:
    with open ("studiestuff.txt", "w") as fil:
        
        
        fil.write("Emner\n")
        for emne in emner:
            fil.write(f"- {emne}\n")

except FileNotFoundError:
    print("fant ikke flien")
