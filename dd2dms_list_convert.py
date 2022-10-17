import pandas as pd


def decdeg2dms(dd):
    mult = -1 if dd < 0 else 1
    mnt, sec = divmod(abs(dd) * 3600, 60)
    deg, mnt = divmod(mnt, 60)
    return f'{int(deg)}°{int(mnt)}\'{round(sec,2)}"'


def dms2decdeg(deg, mnt=0, sec=0):
    mult = -1 if deg < 0 else 1
    dd = (abs(deg) + (mnt / 60) + (sec / 3600)) * mult
    return dd


df = pd.read_csv('coords_original.txt', sep='\t', decimal=",")

for i in df.index:
    print(f"{decdeg2dms(df['Lat'][i])}S {decdeg2dms(df['Lon'][i])}W")

