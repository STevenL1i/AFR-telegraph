import matplotlib
from matplotlib import pyplot as plt
import numpy as np

import connectserver

db = connectserver.connectserver()
cursor = db.cursor()

rank_final = []
rank_lap1 = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

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

query = """SELECT teamName as Team, participants.name as driver, lapNum, carPosition,
                    sector1TimeInStr as S1, sector2TimeInStr as S2, sector3TimeInStr as S3,
                    totalTimeInStr as totalTime, driverStatusChar as driverStatus
            FROM participants_frame INNER JOIN participants
            ON participants.sessionUID=participants_frame.sessionUID
            AND participants.frameIdentifier=participants_frame.frameIdentifier
                        INNER JOIN LapDetail_frame
            ON LapDetail_frame.sessionUID = participants_frame.sessionUID
                        INNER JOIN LapDetail
            ON LapDetail.sessionUID=LapDetail_frame.sessionUID
            AND LapDetail.carIndex= participants.driver_index
            WHERE LapDetail.carIndex =
                (SELECT carIndex FROM LapDetail_frame INNER JOIN LapDetail
                        ON LapDetail.sessionUID=LapDetail_frame.sessionUID
                        AND LapDetail.frameIdentifier=LapDetail_frame.frameIdentifier
                    WHERE carPosition = 1)"""
cursor.execute(query)
result = cursor.fetchall()
racelength = len(result)


fig, ax = plt.subplots(figsize=(24,12))

plt.xlim(1,racelength)
plt.ylim(21,0)

ax.xaxis.set_major_locator(plt.MultipleLocator(1))
ax.yaxis.set_major_locator(plt.MultipleLocator(1))

ax.yaxis.set_major_formatter(plt.FuncFormatter(lap1_rank_and_name))

ax.tick_params(axis="x", bottom=True, top=True, labelbottom=True, labeltop=True, pad = 2)

ax_2 = ax.twinx()
ax_2.set_ylim(21, 0)
ax_2.yaxis.set_major_locator(plt.MultipleLocator(1))
ax_2.yaxis.set_major_formatter(plt.FuncFormatter(final_rank_and_name))

# ax.tick_params(axis="y", left=True, right=True, labelleft=True, labelright=True)

ax.set_title("Rank", loc="left")
ax.set_xlabel("Lap Number")

for i in range(1, 21):
    query = f'SELECT teamName as Team, participants.name as driver, lapNum, carPosition, \
                    sector1TimeInStr as S1, sector2TimeInStr as S2, sector3TimeInStr as S3, \
                    totalTimeInStr as totalTime, driverStatusChar as driverStatus \
            FROM participants_frame INNER JOIN participants \
            ON participants.sessionUID=participants_frame.sessionUID \
            AND participants.frameIdentifier=participants_frame.frameIdentifier \
                        INNER JOIN LapDetail_frame \
            ON LapDetail_frame.sessionUID = participants_frame.sessionUID \
                        INNER JOIN LapDetail \
            ON LapDetail.sessionUID=LapDetail_frame.sessionUID \
            AND LapDetail.carIndex= participants.driver_index \
            WHERE LapDetail.carIndex = \
                (SELECT carIndex FROM LapDetail_frame INNER JOIN LapDetail \
                        ON LapDetail.sessionUID=LapDetail_frame.sessionUID \
                        AND LapDetail.frameIdentifier=LapDetail_frame.frameIdentifier \
                    WHERE carPosition = {i})'
    cursor.execute(query)
    result = cursor.fetchall()

    lap = []
    pos = []
    name = ""

    for Lap in result:
        name = Lap[1]
        lap.append(Lap[2])
        pos.append(Lap[3])
        if result.index(Lap) == 0:
            rank_final.append(name)
            rank_lap1[Lap[3]-1] = name

    
    ax.plot(lap, pos, linewidth=3)

plt.grid(True)
plt.rcParams['savefig.dpi'] = 300
# plt.show()
plt.savefig('position.png', format='png')

# 关闭数据库连接
db.close()
