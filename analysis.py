from audioop import avg
import csv
import tkinter
from tkinter import filedialog

from numpy import average

import convertor as cv

lapfile = []
root = tkinter.Tk()
root.withdraw()


while True:
    filepath = filedialog.askopenfilename()
    
    if filepath.replace(" ", "") == "":
        break
    
    lapfile.append(filepath)
    print(f'laptime file {filepath} imported')


# lapfile = ['F:/Document/Programming/AFR telegraph/laptimedata/STeven L2i (MH).csv']

nameA = []
lapA = []
laptimeA = []
statusA = []

for filepath in lapfile:
    name = ""
    with open(filepath, "r") as lap:
        reader = csv.DictReader(lap)

        lap = []
        laptime = []
        status = []
        for row in reader:
            name = row.get("driverName")
            lap.append(row.get("LapNum"))
            laptime.append(cv.strToLaptime(row.get("Laptime")))
            status.append(row.get("status"))

        nameA.append(name)
        lapA.append(lap)
        laptimeA.append(laptime)
        statusA.append(status)


for i in range(0, len(nameA)):
    name = nameA[i]
    lap = lapA[i]
    laptime = laptimeA[i]
    status = statusA[i]

    print(f'{"Driver:":<10}{name}')
    print()

    inlap, outlap = [], [1]
    for i in range(0, len(status)):
        if i+1 == len(status):
            inlap.append(i+2)
        elif status[i] == "In Lap":
            inlap.append(i+1)
            outlap.append(i+2)
    
    for i in range(0, len(outlap)):
        print(f'Stint {i+1}: Lap {outlap[i]} - {inlap[i]}')
        lapstint = lap[outlap[i] : inlap[i]-1]
        laptimestint = laptime[outlap[i] : inlap[i]-1]
        print(f'fastest lap: {cv.laptimeToStr(min(laptimestint))}')
        print(f'slowest lap: {cv.laptimeToStr(max(laptimestint))}')
        print(f'stint delta: {max(laptimestint) - min(laptimestint):.3f}')
        print(f'stint Avg. : {cv.laptimeToStr(average(laptimestint))}')
        print(f'stint S.D. : {cv.standard_deviation(laptimestint):.6f}')
        print()

    print(f'Total time : {cv.laptimeToStr(sum(laptime))}')
    print("\n\n")