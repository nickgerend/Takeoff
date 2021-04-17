# Written by: Nick Gerend, @dataoutsider
# Viz: "Takeoff", enjoy!

import pandas as pd
import os
from dataoutsider import pie_tree as pt

df2020 = pd.read_csv(os.path.dirname(__file__) + '/aircraft_2020.csv', dtype=pd.StringDtype())
groupers = ['Registrant', 'Aircraft', 'Engine', 'seats_bin']

df_all = pt.pie_tree(df2020, groupers, 1.5, 2., 0., 360., 200, default_sort = False, default_sort_override = True, default_sort_override_reversed = True, all_vertical = False)
df_1 = pt.pie_tree(df2020, groupers, 2.04, 2.1, 0., 360., 100, default_sort = False, default_sort_override = True, default_sort_override_reversed = True, all_vertical = True)

df_all['type'] = 'Mixed'
df_1['type'] = 'Vertical'

df_all['section'] = 1
df_1['section'] = 2

list_df = []
list_df.append(df_all)
list_df.append(df_1)

df_out = pd.concat(list_df, axis=0)
df_out.to_csv(os.path.dirname(__file__) + '/pie_tree.csv', encoding='utf-8', index=False)

groupers2 = ['Registrant', 'STATE', 'NO-ENG', 'speed_bin']
df_out2 = pt.pie_tree(df2020, groupers2, 1.0, 2., 0., 90., 200, default_sort = False, default_sort_override = True, default_sort_override_reversed = True, all_vertical = False)
df_out2.to_csv(os.path.dirname(__file__) + '/pie_tree2.csv', encoding='utf-8', index=False)

print('finished')