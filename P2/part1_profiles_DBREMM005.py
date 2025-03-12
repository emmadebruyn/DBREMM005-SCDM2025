# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 11:17:17 2025

@author: emmak
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 11:39:06 2025

@author: emmak
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
print(os.getcwd())
data = pd.read_csv('CTD_Data_Processed.csv')
depth = data["Depth"]
temperature = data["Temperature (°C)"]
salinity = data["Salinity (psu)"]
fig, axes = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(10, 6))
axes[0].plot(temperature, depth, color='red', linestyle='-')
axes[0].set_xlabel("Temperature (°C)")
axes[0].set_ylabel("Depth (m)")
axes[0].invert_yaxis()
axes[0].set_title("Temperature Profile")
axes[1].plot(salinity, depth, color='blue', linestyle='-')
axes[1].set_xlabel("Salinity (psu)")
axes[1].set_title("Salinity Profile")
plt.tight_layout()
plt.show()
fig.savefig("temperature_salinity_profiles.png", dpi=300)
