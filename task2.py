# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 12:25:40 2021

@author: ilyan
"""

word = input("Введите слово для подсчета букав: ")
gl = 0
sogl = 0
for i in word:
    bukava = i.lower()
    if (bukava == "a" or bukava == "e" or\
       bukava == "i" or bukava == "o" or\
       bukava == "u" or bukava == "y" or\
       bukava == "а" or bukava == "я" or\
       bukava == "о" or bukava == "ё" or\
       bukava == "у" or bukava == "ю" or\
       bukava == "ы" or bukava == "и" or\
       bukava == "э" or bukava == "е"):
        gl += 1
    else:
        sogl += 1
print("Гласных: %i\nСогласных: %i" % (gl, sogl))
