# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 23:26:48 2021

@author: ilyan
"""

word1 = input("Введите слово номер 1: ")
word2 = input("Введите слово номер 2: ")
word1 = word1.lower()
word2 = word2.lower()


match = 0
 
common_letters = set(word1) & set(word2)

print("Совпадающих букв:", len(common_letters))
print("Коэффицент похожести:", len(common_letters) / (len(word1) + len(word2) - len(common_letters)))
        