### user import race lap time data until user cancelled


import csv
import tkinter
from tkinter import filedialog

import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np

lapfile = []
root = tkinter.Tk()
root.withdraw()

while True:
    filepath = filedialog.askopenfilename()
    
    if filepath.replace(" ", "") == "":
        break
    
    lapfile.append(filepath)
    print(f'laptime file {filepath} imported')


fig, ax = plt.subplots(figsize=(12,8))
ax.xaxis.set_major_locator(plt.MultipleLocator(1))
ax.yaxis.set_major_locator(plt.MultipleLocator(1))

ax.xaxis.set_major_locator(plt.MultipleLocator(1))
ax.yaxis.set_major_locator(plt.MultipleLocator(1))

def lap1_rank_and_name(value, tick_number):
    mins = int(int(value)/60)
    second = int(value) - 60*int(mins)
    return "%d:%02d" % (mins, second)

ax.yaxis.set_major_formatter(plt.FuncFormatter(lap1_rank_and_name))

ax.tick_params(axis="x", bottom=True, top=True, labelbottom=True, labeltop=True, pad = 2)

ax.set_title("Lap", loc="left")
ax.set_xlabel("Lap Number")

for filepath in lapfile:
    name = ""
    with open(filepath, "r") as lap:
        reader = csv.DictReader(lap)

        lap = []
        laptime = []
        for row in reader:
            name = row.get("driverName")
            laptimeStr = row.get("Laptime")
            try:
                float(laptimeStr)
            except ValueError:
                lt = int(laptimeStr[:laptimeStr.find(":")]) * 60
                lt += int(laptimeStr[laptimeStr.find(":")+1:laptimeStr.find(".")])
                lt += int(laptimeStr[laptimeStr.find(".")+1:]) / 1000
                laptime.append(lt)
                lap.append(row.get("LapNum"))
        
        #lap.pop()
        #laptime.pop()

        ax.plot(lap, laptime, label=(f'{name}'), linewidth=2)

plt.grid(True)
ax.legend(frameon=False)

# plt.show()

plt.savefig("laptimedata/laptime.png", format="png")