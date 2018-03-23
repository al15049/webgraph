#!/usr/bin/env python3
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("sensorData.csv", names=['Vol', 'chars'])
print(df.describe())
plt.plot(range(0,1000),df['chars'],marker="o")
plt.title('Nakajima Laboratory')
plt.xlabel('time')
plt.ylabel('taizai')
plt.savefig("sin2.png")

html_body = """
<html><body>
<img src= "../sin2.png">
</body></html>
"""

print("Content-type: text/html\n")
print(html_body)
