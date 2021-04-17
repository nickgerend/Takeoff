# Written by: Nick Gerend, @dataoutsider
# Viz: "Takeoff", enjoy!

import pandas as pd
import os
from datetime import datetime

# df_m = pd.read_csv(os.path.dirname(__file__) + '/MASTER.csv', dtype=pd.StringDtype())
# df_a = pd.read_csv(os.path.dirname(__file__) + '/ACFTREF.csv', dtype=pd.StringDtype())
# df_a.rename(columns={'MFR': 'MFR_Aircraft', 'MODEL': 'Model_Aircraft'}, inplace=True)
# df_e = pd.read_csv(os.path.dirname(__file__) + '/ENGINE.csv', dtype=pd.StringDtype())
# df_e.rename(columns={'MFR': 'MFR_Engine', 'MODEL': 'Model_Engine'}, inplace=True)
# df_lookup = pd.read_csv(os.path.dirname(__file__) + '/Lookup.csv', dtype=pd.StringDtype())
# df = pd.merge(df_m, df_a, how='left', left_on=['MFR MDL CODE'], right_on = ['CODE'])
# df = pd.merge(df, df_e, how='left', left_on=['ENG MFR MDL'], right_on = ['CODE'])

# df = df[['YEAR MFR', 'TYPE REGISTRANT', 'NAME', 'CITY', 'STATE', 'ZIP CODE', 'COUNTRY', 'TYPE AIRCRAFT', 'TYPE ENGINE', 'STATUS CODE', 'AIR WORTH DATE', 'EXPIRATION DATE', 'MFR_Aircraft', 'Model_Aircraft', 'AC-CAT', 'NO-ENG', 'NO-SEATS', 'AC-WEIGHT', 'SPEED', 'MFR_Engine', 'Model_Engine', 'HORSEPOWER', 'THRUST']]

# df['TYPE ENGINE'] = df['TYPE ENGINE'].astype(int)

# df_Reg = df_lookup.loc[df_lookup['Column']=='Registrant']
# df_Reg.rename(columns={'Column': 'Column_1', 'Value': 'Registrant', 'Code': 'Code_1'}, inplace=True)
# df_Cat = df_lookup.loc[df_lookup['Column']=='Category']
# df_Cat.rename(columns={'Column': 'Column_2', 'Value': 'Category', 'Code': 'Code_2'}, inplace=True)
# df_Wei = df_lookup.loc[df_lookup['Column']=='Weight']
# df_Wei.rename(columns={'Column': 'Column_3', 'Value': 'Weight', 'Code': 'Code_3'}, inplace=True)
# df_Air = df_lookup.loc[df_lookup['Column']=='Aircraft']
# df_Air.rename(columns={'Column': 'Column_4', 'Value': 'Aircraft', 'Code': 'Code_4'}, inplace=True)
# df_Eng = df_lookup.loc[df_lookup['Column']=='Engine']
# df_Eng.rename(columns={'Column': 'Column_5', 'Value': 'Engine', 'Code': 'Code_5'}, inplace=True)
# df_Eng['Code_5'] = df_Eng['Code_5'].astype(int)

# df = pd.merge(df, df_Reg, how='left', left_on=['TYPE REGISTRANT'], right_on = ['Code_1'])
# df = pd.merge(df, df_Cat, how='left', left_on=['AC-CAT'], right_on = ['Code_2'])
# df = pd.merge(df, df_Wei, how='left', left_on=['AC-WEIGHT'], right_on = ['Code_3'])
# df = pd.merge(df, df_Air, how='left', left_on=['TYPE AIRCRAFT'], right_on = ['Code_4'])
# df = pd.merge(df, df_Eng, how='left', left_on=['TYPE ENGINE'], right_on = ['Code_5'])

# df = df[['YEAR MFR', 'NAME', 'CITY', 'STATE', 'ZIP CODE', 'COUNTRY', 'STATUS CODE', 'AIR WORTH DATE', 'EXPIRATION DATE', 'MFR_Aircraft', 'Model_Aircraft', 'NO-ENG', 'NO-SEATS', 'SPEED', 'MFR_Engine', 'Model_Engine', 'HORSEPOWER', 'THRUST', 'Registrant', 'Category', 'Weight', 'Aircraft', 'Engine']]
# df.reset_index(level=0, inplace=True)

# df['NO-SEATS'] = df['NO-SEATS'].astype(int)
# bins = [0, 5, 10, 25, 50, 100, 250, 500, 1000]
# df['seats_bin'] = pd.cut(df['NO-SEATS'], bins)

# df['SPEED'] = df['SPEED'].astype(float)
# bins2 = [-5., 0., 100., 200., 300., 400., 500.]
# df['speed_bin'] = pd.cut(df['SPEED'], bins2)

# df.to_csv(os.path.dirname(__file__) + '/aircraft.csv', encoding='utf-8', index=False)

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

df_2020['speed_bin'] = ['Unknown' if '-5.0' in x else x for x in df_2020['speed_bin']]

df_2020.to_csv(os.path.dirname(__file__) + '/aircraft_2020.csv', encoding='utf-8', index=False)

print('finished')