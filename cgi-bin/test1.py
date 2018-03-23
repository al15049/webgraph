#!/usr/bin/env python3
import datetime
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("mmchars.csv", names=['Vol', 'chars'])
print(df.describe())
plt.plot(range(0,241),df['chars'],marker="o")
plt.title('Nakajima Laboratory')
plt.xlabel('time')
plt.ylabel('taizai')
plt.savefig("sin.png")

html_body = """
<html><body>
{0.year:d}/{0.month:d}/{0.day:d} {0.hour:d}:{0.minute:d}:{0.second:d}
<img src= "../sin.png">
</body></html>
"""

now=datetime.datetime.now()

print("Content-type: text/html\n")

