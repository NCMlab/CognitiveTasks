# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 21:18:24 2022

@author: steff
"""
import os
_thisDir = os.path.normpath(os.path.dirname(os.path.abspath(__file__)))
print(_thisDir)
path = os.path.dirname(_thisDir)
print(path)
print(os.path.join(path, "ConfigFiles"))
