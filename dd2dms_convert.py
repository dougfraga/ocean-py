def decdeg2dms(dd):
    """Converts from decimal degree coordinates format to degree, minutes and seconds format"""
    mult = -1 if dd < 0 else 1
    mnt, sec = divmod(abs(dd) * 3600, 60)
    deg, mnt = divmod(mnt, 60)
    return f'{int(deg)}°{int(mnt)}\'{round(sec,2)}"'


def dms2decdeg(deg, mnt=0, sec=0):
    """Converts from degree, minutes and seconds coordinates format to decimal degree format"""
    mult = -1 if deg < 0 else 1
    dd = (abs(deg) + (mnt / 60) + (sec / 3600)) * mult
    return dd


if __name__ == '__main__':
    print(f'latitude {dms2decdeg(-22, 42, 6.612)}S e longitude {dms2decdeg(-40, 40, 37.583)}W')

