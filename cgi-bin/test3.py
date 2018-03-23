#!/usr/bin/env python3
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("sensorData.csv",names=['dataTime','unixTime','lux'])
df2 = df['lux'].values.tolist()
i=0
while i < 1000:
    if df2[i] <= 400:
        df2[i] = 0
    elif df2[i] > 400:
        df2[i] = 1
    i = i+1

print(df2) 

print(df.describe())
plt.plot(range(0,1000),df2)
plt.title('Nakajima Laboratory')
plt.xlabel('time')
plt.ylabel('stay')
plt.savefig("sin3.png")

html_body = """
<html><body>
<img src= "../sin3.png">
</body></html>
"""

print("Content-type: text/html\n")
print(html_body)

