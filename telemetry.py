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


############## throttle plot ###############
fig, ax = plt.subplots(figsize=(64,16))

plt.ylim(0,1.05)

ax.xaxis.set_major_locator(plt.MultipleLocator(100))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.1))

ax.tick_params(axis="x", bottom=True, top=True, labelbottom=True, labeltop=False, pad = 2)

ax.set_title("Distance", loc="left")
ax.set_xlabel("Lap Distance")
ax.set_ylabel("throttle")

for filepath in telefile:
    name = ""
    with open(filepath, "r") as tele:
        reader = csv.DictReader(tele)

        LapDistance = []
        throttle = []
        for row in reader:
            if row.get("name") == "":
                continue
            name = row.get("name")
            distance = float(f'{float(row.get("LapDistance")):.4f}')
            LapDistance.append(distance)
            th = float(f'{float(row.get("throttle")):.4f}')
            throttle.append(th)

        ax.plot(LapDistance, throttle, label=(f'{name}'), linewidth=2)


plt.grid(True)
ax.legend(frameon=True)

# plt.show()

plt.savefig("telemetrydata/telemetry(power).png", format="png")



############## braking plot ###############
fig2, ax2 = plt.subplots(figsize=(64,16))

plt.ylim(0,1.05)

ax2.xaxis.set_major_locator(plt.MultipleLocator(100))
ax2.yaxis.set_major_locator(plt.MultipleLocator(0.1))

ax2.tick_params(axis="x", bottom=True, top=True, labelbottom=True, labeltop=False, pad=2)

ax2.set_title("Distance", loc="left")
ax2.set_xlabel("Lap Distance")
ax2.set_ylabel("brake")

for filepath in telefile:
    name = ""
    with open(filepath, "r") as tele:
        reader = csv.DictReader(tele)

        LapDistance = []
        brake = []
        for row in reader:
            if row.get("name") == "":
                continue
            name = row.get("name")
            distance = float(f'{float(row.get("LapDistance")):.4f}')
            LapDistance.append(distance)
            b = float(f'{float(row.get("brake")):.4f}')
            brake.append(b)

        ax2.plot(LapDistance, brake, label=(f'{name}'), linewidth=2)


plt.grid(True)
ax2.legend(frameon=True)

plt.savefig("telemetrydata/telemetry(brake).png", format="png")





############## gear plot ###############
fig3, ax3 = plt.subplots(figsize=(64,16))

plt.ylim(0,9)

ax3.xaxis.set_major_locator(plt.MultipleLocator(100))
ax3.yaxis.set_major_locator(plt.MultipleLocator(1))

ax3.tick_params(axis="x", bottom=True, top=True, labelbottom=True, labeltop=False, pad=2)

ax3.set_title("Distance", loc="left")
ax3.set_xlabel("Lap Distance")
ax3.set_ylabel("gear")

for filepath in telefile:
    name = ""
    with open(filepath, "r") as tele:
        reader = csv.DictReader(tele)

        LapDistance = []
        gear = []
        for row in reader:
            if row.get("name") == "":
                continue
            name = row.get("name")
            distance = float(f'{float(row.get("LapDistance")):.4f}')
            LapDistance.append(distance)
            g = int(row.get("gear"))
            gear.append(g)

        ax3.plot(LapDistance, gear, label=(f'{name}'), linewidth=2)


plt.grid(True)
ax3.legend(frameon=True)

plt.savefig("telemetrydata/telemetry(gear).png", format="png")



############## steer plot ###############
fig4, ax4 = plt.subplots(figsize=(64,16))

plt.ylim(-1,1)

ax4.xaxis.set_major_locator(plt.MultipleLocator(100))
ax4.yaxis.set_major_locator(plt.MultipleLocator(0.1))

ax4.tick_params(axis="x", bottom=True, top=True, labelbottom=True, labeltop=False, pad=2)

ax4.set_title("Distance", loc="left")
ax4.set_xlabel("Lap Distance")
ax4.set_ylabel("steer")

for filepath in telefile:
    name = ""
    with open(filepath, "r") as tele:
        reader = csv.DictReader(tele)

        LapDistance = []
        steer = []
        for row in reader:
            if row.get("name") == "":
                continue
            name = row.get("name")
            distance = float(f'{float(row.get("LapDistance")):.4f}')
            LapDistance.append(distance)
            s = float(f'{float(row.get("steer")):.4f}')
            steer.append(s)

        ax4.plot(LapDistance, steer, label=(f'{name}'), linewidth=2)


plt.grid(True)
ax4.legend(frameon=True)

plt.savefig("telemetrydata/telemetry(steer).png", format="png")



############## speed plot ###############
fig5, ax5 = plt.subplots(figsize=(64,16))

plt.ylim(0, 360)

ax5.xaxis.set_major_locator(plt.MultipleLocator(100))
ax5.yaxis.set_major_locator(plt.MultipleLocator(10))

ax5.tick_params(axis="x", bottom=True, top=True, labelbottom=True, labeltop=False, pad=2)

ax5.set_title("Distance", loc="left")
ax5.set_xlabel("Lap Distance")
ax5.set_ylabel("speed")

for filepath in telefile:
    name = ""
    with open(filepath, "r") as tele:
        reader = csv.DictReader(tele)

        LapDistance = []
        speed = []
        for row in reader:
            if row.get("name") == "":
                continue
            name = row.get("name")
            distance = float(f'{float(row.get("LapDistance")):.4f}')
            LapDistance.append(distance)
            s = float(f'{float(row.get("speed")):.4f}')
            speed.append(s)

        ax5.plot(LapDistance, speed, label=(f'{name}'), linewidth=2)


plt.grid(True)
ax5.legend(frameon=True)

plt.savefig("telemetrydata/telemetry(speed).png", format="png")