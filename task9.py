# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 21:36:36 2021

@author: ilyan
"""

import numpy as np

island_raw = np.loadtxt('island.txt', dtype=str)
island = np.empty(len(island_raw), dtype=int)
for (i in range(len(island_raw))):
    island[i] = ord(island_raw[i])
