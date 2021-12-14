# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 12:25:40 2021

@author: ilyan
"""

word = input("Введите слово для подсчета букв: ")
glas = 0
sogl = 0
vowels = "aeiouаяоеуюыиэе"
for i in word:
    ba = i.lower()
    if (i in vowels):
        glas += 1
    else:
        sogl += 1
print("Гласных: %i\nСогласных: %i" % (glas, sogl))
