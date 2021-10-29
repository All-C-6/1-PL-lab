# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 12:42:32 2021

@author: ilyan
"""
maxx = 0
maxx_word = " "
txt = open('words.txt')

for line in txt:
    if (len(line) > maxx):
        maxx = len(line)
        maxx_word = line

print("Самое длинное слово в файле: %s имеет длину: %i" % (maxx_word, maxx))