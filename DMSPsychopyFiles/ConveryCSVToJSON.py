#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 21:36:05 2021

@author: jasonsteffener
"""
import json
import pandas as pd

P = 'DMSBlockListMRIRun2.csv'
df = pd.read_csv(P)
for index, row in df.iterrows():
    StimLetters = ''
    for j in range(9):
        StimLetters += row[j]
    
    if (row[10] == 'right'):
        Correct=False
    else:
        Correct=True
            
    x = {"StimulusLetters":StimLetters,
         "ProbeLetter": row[9],
         "Correct":Correct,
         "Load":row[11]}
    print(json.dumps(x)+",")
    
            
        