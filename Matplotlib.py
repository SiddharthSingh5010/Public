import os
import pandas as pd
import sys
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\TS.csv")
df['Number'][0]=340
df['Number'][2]=430
date=df['Date'].head()
number=df['Number'].head()
fig = plt.figure(figsize =(10, 7))
plt.bar(date[0:4], number[0:4])
plt.title("MY FIRST PLOT",fontsize=30)
plt.savefig("F:\\PT.JPEG",dpi=100,format="jpeg")
#os.execv("C:\\WINDOWS\\SYSTEM32\\MSPAINT.EXE",["-OPEN F:\\PT.JPEG"])
df1=pd.read_csv("F:\\Siddharth\\Jupyter\\Files\\TestData.csv")
df1.reset_index(drop=True,inplace=True)
df1=df1.loc[df1['Game']=='Race Cars']
print(df1)