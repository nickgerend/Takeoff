# Written by: Nick Gerend, @dataoutsider
# Viz: "Takeoff", enjoy!

import pandas as pd
import numpy as np
import os
from datetime import datetime
from math import pi, cos, sin, sqrt

df = pd.read_csv(os.path.dirname(__file__) + '/aircraft.csv', dtype=pd.StringDtype())

df['AIR WORTH DATE'] = df['AIR WORTH DATE'].str.strip()
df_2020 = df.loc[(df['AIR WORTH DATE'].notnull()) & (df['AIR WORTH DATE']!='')]

df_2020['A_W_Date'] = [datetime.strptime(t, '%Y%m%d') for t in df_2020['AIR WORTH DATE']]
df_2020['A_W_Date_Year'] = df_2020['A_W_Date'].dt.year

df_2020 = df_2020.loc[(df_2020['A_W_Date_Year'] == 2020)]

df_2020['Registrant'] = df_2020['Registrant'].str.strip()
df_2020 = df_2020.loc[(df_2020['Registrant'].notnull()) & (df_2020['Registrant']!='')]

df_2020['Aircraft'] = df_2020['Aircraft'].str.strip()
df_2020 = df_2020.loc[(df_2020['Aircraft'].notnull()) & (df_2020['Aircraft']!='')]

df_2020['Engine'] = df_2020['Engine'].str.strip()
df_2020 = df_2020.loc[(df_2020['Engine'].notnull()) & (df_2020['Engine']!='')]

df_2020['seats_bin'] = df_2020['seats_bin'].str.strip()
df_2020 = df_2020.loc[(df_2020['seats_bin'].notnull()) & (df_2020['seats_bin']!='')]

df_2020['MFR_Aircraft'] = df_2020['MFR_Aircraft'].str.strip()
df_2020['MFR_Engine'] = df_2020['MFR_Engine'].str.strip()

df_2020.to_csv(os.path.dirname(__file__) + '/aircraft_2020.csv', encoding='utf-8', index=False)

print('finished')