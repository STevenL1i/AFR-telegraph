import csv
import convertor as cv


# 圈速1
name1 = ""
lap1 = []
laptime1 = []
with open("Head brother (MS).csv", "r") as lap:
    reader = csv.DictReader(lap)

    for row in reader:
        name1 = row.get("driverName")
        lap1.append(row.get("LapNum"))
        laptimeStr = row.get("Laptime")
        laptime1.append(cv.strToLaptime(laptimeStr))


# 圈速2
name2 = ""
lap2 = []
laptime2 = []
with open("STeven L2i (MH).csv", "r") as lap:
    reader = csv.DictReader(lap)

    for row in reader:
        name2 = row.get("driverName")
        lap2.append(row.get("LapNum"))
        laptimeStr = row.get("Laptime")
        laptime2.append(cv.strToLaptime(laptimeStr))


medium1 = laptime1[31:52]
medium2 = laptime2[25:52]

fl1 = min(medium1)
sl1 = max(medium1)
fl2 = min(medium2)
sl2 = max(medium2)

print(f'{name1 + " FL":<30}{cv.laptimeToStr(fl1)}')
print(f'{name1 + " SL":<30}{cv.laptimeToStr(sl1)}')
print(f'{name1 + " delta":<30}{sl1-fl1:.4f}')
print()
print(f'{name2 + " FL":<30}{cv.laptimeToStr(fl2)}')
print(f'{name2 + " SL":<30}{cv.laptimeToStr(sl2)}')
print(f'{name2 + " delta":<30}{sl2-fl2:.4f}')
print()

medium1 = laptime1[31:52]
medium2 = laptime2[25:52]

print(f'{name1 + " sd:":<30}{cv.standard_deviation(medium1)}')
print(f'{name2 + " sd:":<30}{cv.standard_deviation(medium2)}')
print()


medium1 = laptime1
medium2 = laptime2


totaltime1 = sum(medium1)
totaltime2 = sum(medium2)

print(f'{name1 + " TT:":<30}{cv.laptimeToStr(totaltime1)}')
print(f'{name2 + " TT:":<30}{cv.laptimeToStr(totaltime2)}')
print(f'{"delta:":<30}{totaltime1-totaltime2:.3f}')
print()