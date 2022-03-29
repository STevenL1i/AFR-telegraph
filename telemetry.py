### user import telemetry data until user cancelled


import csv
import tkinter
from tkinter import filedialog

import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np

telefile = []
root = tkinter.Tk()
root.withdraw()

while True:
    filepath = filedialog.askopenfilename()
    
    if filepath.replace(" ", "") == "":
        break
    
    telefile.append(filepath)
    print(f'laptime file {filepath} imported')


fig, ax = plt.subplots(figsize=(96,48))
plt.ylim(0,1.05)

ax.xaxis.set_major_locator(plt.MultipleLocator(1))
ax.yaxis.set_major_locator(plt.MultipleLocator(1))

ax.xaxis.set_major_locator(plt.MultipleLocator(1))
ax.yaxis.set_major_locator(plt.MultipleLocator(1))

ax.tick_params(axis="x", bottom=True, top=True, labelbottom=True, labeltop=True, pad = 2)

ax.set_title("Time", loc="left")
ax.set_xlabel("Time line")
ax.set_ylabel("throttle")

for filepath in telefile:
    name = ""
    with open(filepath, "r") as tele:
        reader = csv.DictReader(tele)

        time = []
        throttle = []
        for row in reader:
            name = row.get("name")
            time.append(row.get("frame"))
            throttle.append(float(f'{row.get("throttle"):.4}'))

        ax.plot(time, throttle, label=(f'{name}'), linewidth=2)


plt.grid(True)
ax.legend(frameon=True)

# plt.show()

plt.savefig("telemetrydata/telemetry.png", format="png")