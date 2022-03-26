import csv

import matplotlib as mpl
from matplotlib import pyplot as plt
import numpy as np


lapST = []
laptimeST = []
lapM4 = []
laptimeM4 = []

with open("data/h0.csv", "r") as lap:
    reader = csv.DictReader(lap)

    for row in reader:
        lapST.append(row.get("LapNum"))
        laptime_str = row.get("Laptime")
        laptime = int(laptime_str[:laptime_str.find(":")]) * 60
        laptime += int(laptime_str[laptime_str.find(":")+1:laptime_str.find(".")])
        laptime += int(laptime_str[laptime_str.find(".")+1:]) / 1000
        laptimeST.append(laptime)

with open("data/wofa.csv", "r") as lap:
    reader = csv.DictReader(lap)

    for row in reader:
        lapM4.append(row.get("LapNum"))
        laptime_str = row.get("Laptime")
        laptime = int(laptime_str[:laptime_str.find(":")]) * 60
        laptime += int(laptime_str[laptime_str.find(":")+1:laptime_str.find(".")])
        laptime += int(laptime_str[laptime_str.find(".")+1:]) / 1000
        laptimeM4.append(laptime)


fig, ax = plt.subplots(figsize=(12,8))

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

ax.plot(lapST, laptimeST, label=("%d: %s" % (1, "h0")), linewidth=2)
ax.plot(lapM4, laptimeM4, label=("%d: %s" % (2, "wofa")), linewidth=2)

plt.grid(True)
ax.legend(frameon=False)

plt.show()

plt.savefig('./laptime.png', format='png')
