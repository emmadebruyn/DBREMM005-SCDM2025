# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 14:06:21 2025

@author: emmak
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # For better-looking plots
data = pd.read_csv("SAA2_WC_2017_metocean_10min_avg.csv", parse_dates=["TIME_SERVER"])
print(data.columns)
print(data.isnull().sum())
data_filtered = data[data["time_column"] <= "2017-07-04"]
data_filtered = data[data["time_column"] <= "2017-07-04"]
print(data_filtered["TIME_SERVER"].min(), data_filtered["TIME_SERVER"].max())  # Check date range
plt.style.use("grayscale")
plt.figure(figsize=(10, 5))
plt.plot(data_filtered["TIME_SERVER"], data_filtered["TSG_TEMP"], linestyle="-", color="black")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Water temperature Over Time")
plt.xticks(rotation=45)
plt.savefig("temperature_timeseries.png", dpi=300)
plt.show()
plt.figure(figsize=(8, 5))
plt.hist(data_filtered["TSG_SALINITY"], bins=np.arange(30, 35.5, 0.5), color="blue", edgecolor="black")
plt.xlabel("Salinity (psu)")
plt.ylabel("Frequency")
plt.title("Salinity Distribution")
plt.savefig("salinity_histogram.png", dpi=300)
plt.show()
temp_mean = data_filtered["TSG_TEMP"].mean()
temp_std = data_filtered["TSG_TEMP"].std()
temp_iqr = data_filtered["TSG_TEMP"].quantile(0.75) - data_filtered["TSG_TEMP"].quantile(0.25)
sal_mean = data_filtered["TSG_SALINITY"].mean()
sal_std = data_filtered["TSG_SALINITY"].std()
sal_iqr = data_filtered["TSG_SALINITY"].quantile(0.75) - data_filtered["TSG_SALINITY"].quantile(0.25)
stats = pd.DataFrame({
"Variable": ["Temperature", "Salinity"],
"Mean": [temp_mean, sal_mean],
"Standard Deviation": [temp_std, sal_std],
"Interquartile Range": [temp_iqr, sal_iqr]
})
print(stats)
stats.to_csv("stats_table.csv", index=False)
plt.figure(figsize=(8, 5))
plt.colorbar(label="Latitude")
plt.xlabel("Wind Speed (m/s)")
plt.ylabel("Air Temperature (°C)")
plt.title("Wind Speed vs Air Temperature")
plt.savefig("wind_vs_temp.png", dpi=300)
plt.show()
runcell(0, 'C:/Users/emmak/OneDrive - University of Pretoria/Desktop/UCT WORK/SCDM/P2/untitled2.py')

