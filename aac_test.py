import tkinter
from tkinter import X, filedialog
import pandas
from sklearn import linear_model


root = tkinter.Tk()
root.withdraw()
filepath = filedialog.askopenfilename()
print(f'laptime file {filepath} imported\n\n\n')

df = pandas.read_csv(filepath)

x = df[["LapDistance", "steer", "throttle", "brake", "gear",
        "worldPositionX", "worldPositionY", "worldPositionZ",
        "gForceLateral", "gForceLongitudinal", "gForceVertical"]]
y = df["speed"]

regr = linear_model.LinearRegression()
regr.fit(x, y)

print(regr.coef_)





root = tkinter.Tk()
root.withdraw()
filepath = filedialog.askopenfilename()
print(f'laptime file {filepath} imported\n\n\n')

file = open("predict.csv", "w")
header = list(df.columns)
