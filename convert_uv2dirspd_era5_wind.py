# -*- coding: utf-8 -*-
"""
Read u and v wind components time serie exported from read_era5_wind.py and 
convert to wind speed and direction (meteorological convention)

@author: Douglas Fraga
"""
# Libs
import pandas as pd
import numpy as np


# Import data
path2=r"C:/Users/Asus/Google Drive/Baía de Ilha Grande/ERA5/"
df = pd.read_csv('era5_filt.txt', sep='\t', index_col='Datetime', encoding='utf-8')


# Convert u and v wind components to wind speed and direction
df['dirl'] = np.mod(180 + np.rad2deg(np.arctan2(df['ul'], df['vl'])), 360)
df['spdl'] = np.sqrt(df['ul']**2 + df['vl']**2)
