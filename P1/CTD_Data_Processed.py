

>>> import pandas as pd
>>> df = pd.read_csv("CTD_Data_Processed.csv")
>>> print(df.head())
     11/29/2008\t06:52\t5\t28.97\t35.21
0  11/29/2008  \t06:52\t6\t28.98\t35.21
1    11/29/2008\t06:52\t7\t28.99\t35.21
2    11/29/2008\t06:52\t8\t28.96\t35.21
3    11/29/2008\t06:52\t9\t28.99\t35.21
4   11/29/2008\t06:52\t10\t28.99\t35.21
>>> df = pd.read_csv("CTD_Data_Processed.csv", delimiter="\t", header=None)
>>> df.columns = ["Date", "Time", "Depth (m)", "Temperature (°C)", "Salinity (psu)"]
>>> print(df.head())
           Date   Time  Depth (m)  Temperature (°C)  Salinity (psu)
0    11/29/2008  06:52          5             28.97           35.21
1  11/29/2008    06:52          6             28.98           35.21
2    11/29/2008  06:52          7             28.99           35.21
3    11/29/2008  06:52          8             28.96           35.21
4    11/29/2008  06:52          9             28.99           35.21

