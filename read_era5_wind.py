# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 10:18:06 2020

@author: Douglas Fraga
"""
###############################################################################
# Libs
###############################################################################
from netCDF4 import Dataset
from datetime import timedelta, datetime
from scipy.signal import butter, filtfilt
import numpy as np
import pandas as pd
import math



###############################################################################
# Input geographic coords
###############################################################################
Lat = -23.75  # [-23.  , -23.25, -23.5 , -23.75, -24.]
Lon = -44.03  # [-45.  , -44.75, -44.5 , -44.25, -44.  , -43.75, -43.5 ]


###############################################################################
# Input time interval
###############################################################################
t0 = '1998-09-01 00:00:00'
t1 = '1998-10-30 11:00:00'


###############################################################################
# Read netCDF file
###############################################################################
f = Dataset('era5_data.nc','r')


###############################################################################
# Storing the variables
###############################################################################
# Date vector
time = np.double(f.variables['time'][:])

d0 = datetime.strptime('1900-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')

date = []
for k in time:
    date.append(d0 + timedelta(hours=k))
    
# Geographic coords vector
lat = f.variables['latitude'][:]
lon = f.variables['longitude'][:]

lon, lat = np.meshgrid(lon, lat)

# Find matrix index  
X = np.sqrt( np.square( lat - Lat ) +  np.square( lon - Lon ) )
id = np.where( X == X.min() )

# Variables
u0 = f.variables['u10'][:,id[0],id[1]]
v0 = f.variables['v10'][:,id[0],id[1]]

u0 = np.squeeze(u0)
v0 = np.squeeze(v0)


###############################################################################
# Rotation
###############################################################################
tet = -11
u = (u0*np.cos(math.radians(tet)))-(v0*np.sin(math.radians(tet)))
v = (u0*np.sin(math.radians(tet)))+(v0*np.cos(math.radians(tet)))


###############################################################################
# Create DataFrame
###############################################################################
df = pd.DataFrame({'u':u,'v':v},date)


###############################################################################            
# Low Pass Butterworth Filter
###############################################################################
def freqcuts(cut):
    cutoff = 1.0/(cut*3600*24)
    return cutoff

def butter_pass(cutoff, fs, order):
    cutoff = freqcuts(cut)
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype=typef, analog=False)
    return b, a

def butter_pass_filter(data, cutoff, fs, order):
    b, a = butter_pass(cutoff, fs, order)
    y = filtfilt(b, a, data)
    return y


###############################################################################
# Filter params
###############################################################################
typef = 'low'
cut = 1.6666666667#3 # 3 days
fs = 1.0/(60*60.0)
order = 3
cutoff = freqcuts(cut)

df['ul'] = butter_pass_filter(df['u'], cutoff, fs, order)
df['vl'] = butter_pass_filter(df['v'], cutoff, fs, order)


###############################################################################
# Time interval
###############################################################################
df = df[(df.index >= t0)&(df.index <= t1)]


###############################################################################
# Graphics
###############################################################################
df['ul'].plot()

