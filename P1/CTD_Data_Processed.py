# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 14:33:08 2025

@author: emmak
"""
import pandas as pd 
df = pd.read_csv("CTD_Data_Processed.csv")
print(df.head())
df = pd.read_csv("CTD_Data_Processed.csv", delimiter="\t", header=None)
df.columns = ["Date", "Time", "Depth (m)", "Temperature (°C)", "Salinity (psu)"]
print(df.head())
