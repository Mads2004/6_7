# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 21:39:20 2025

@author: Olli
"""
studieplan= list()
emner= list()

try:
    with open ("studiestuff.txt", "r",encoding=UTTF-8) as fil:
        fil.readline()
        for linje in fil:
            linje = linje.strip()
            