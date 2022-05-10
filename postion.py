### using all driver lap time data in a session


import csv
import os
import tkinter
from tkinter import filedialog

import matplotlib
from matplotlib import pyplot as plt
import numpy as np

"""
import connectserver
db = connectserver.connectserver()
cursor = db.cursor()
"""

rank_final = []
for i in range(0,20):
    rank_final.append("")
rank_lap1 = []
for i in range(0,20):
    rank_lap1.append("")

def lap1_rank_and_name(value, tick_number):
    if tick_number > 1 and tick_number < len(rank_lap1)+2:
        return "%s  %d" % (rank_lap1[tick_number-2], tick_number-1)
    else:
        return "%d" % (tick_number-1)

def final_rank_and_name(value, tick_number):
    if tick_number > 1 and tick_number < len(rank_final)+2:
        return "%d  %s" % (tick_number-1, rank_final[tick_number-2])
    else:
        return "%d" % (tick_number-1)


root = tkinter.Tk()
root.withdraw()

dirpath = filedialog.askdirectory()

filelist = []

for root, dirs, files in os.walk(dirpath):
    for file in files:
        if file.find(".csv") != -1:
            filelist.append(file)

racelength = 0
for file in filelist:
    racelength_test = 0
    with open(f'laptimedata/{file}', "r") as lap:
        reader = csv.DictReader(lap)

        for row in reader:
            racelength_test += 1
        
    if racelength_test > racelength:
        racelength = racelength_test



fig, ax = plt.subplots(figsize=(24,12))

plt.xlim(0,racelength)
plt.ylim(len(filelist)+1,0)

ax.xaxis.set_major_locator(plt.MultipleLocator(1))
ax.yaxis.set_major_locator(plt.MultipleLocator(1))

ax.yaxis.set_major_formatter(plt.FuncFormatter(lap1_rank_and_name))

ax.tick_params(axis="x", bottom=True, top=True, labelbottom=True, labeltop=True, pad = 2)

ax_2 = ax.twinx()
ax_2.set_ylim(len(filelist)+1, 0)
ax_2.yaxis.set_major_locator(plt.MultipleLocator(1))
ax_2.yaxis.set_major_formatter(plt.FuncFormatter(final_rank_and_name))

# ax.tick_params(axis="y", left=True, right=True, labelleft=True, labelright=True)

ax.set_title("Rank", loc="left")
ax.set_xlabel("Lap Number")

for file in filelist:
    lap = []
    pos = []
    name = ""

    with open(f'laptimedata/{file}', "r") as laps:
        reader = csv.DictReader(laps)

        startindex = 0
        for row in reader:
            name = row.get("driverName")
            if startindex == 0:
                lap.append(0)
                startindex = 1
            else:
                lap.append(int(row.get("LapNum")))
            
            pos.append(int(row.get("Position")))



    rank_lap1[pos[0]-1] = name
    rank_final[pos[-1]-1] = name
    
    ax.plot(lap, pos, linewidth=3)


plt.grid(True)
plt.rcParams['savefig.dpi'] = 300
# plt.show()
plt.savefig('laptimedata/position.png', format='png')