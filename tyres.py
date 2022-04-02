### user import tyre data until user cancelled


import csv
import tkinter
from tkinter import filedialog

import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np

tyrefile = []
root = tkinter.Tk()
root.withdraw()

while True:
    filepath = filedialog.askopenfilename()
    
    if filepath.replace(" ", "") == "":
        break
    
    tyrefile.append(filepath)
    print(f'laptime file {filepath} imported')


fig, ax = plt.subplots(figsize=(24,12))
ax.xaxis.set_major_locator(plt.MultipleLocator(10000))
ax.yaxis.set_major_locator(plt.MultipleLocator(5))

ax.tick_params(axis="x", bottom=True, top=True, labelbottom=True, labeltop=True, pad = 2)

ax.set_title("Tyre", loc="left")
ax.set_xlabel("Time Line")

for filepath in tyrefile:
    name = ""
    with open(filepath, "r") as lap:
        reader = csv.DictReader(lap)

        frame = []
        tyre = []
        for row in reader:
            name = row.get("name")
            fl = int(row.get("fl"))
            fr = int(row.get("fr"))
            rl = int(row.get("rl"))
            rr = int(row.get("rr"))
            wear = (fl+fr+rl+rr) / 4
            frame.append(row.get("frameIdentifier"))
            tyre.append(wear)

        ax.plot(frame, tyre, label=(f'{name}'), linewidth=2)


plt.grid(True)
ax.legend(frameon=False)

# plt.show()

plt.savefig("test.png", format="png")