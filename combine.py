# Written by: Nick Gerend, @dataoutsider
# Viz: "Takeoff", enjoy!

import pandas as pd
import os

df_pietree = pd.read_csv(os.path.dirname(__file__) + '/pie_tree.csv')
df_lines = pd.read_csv(os.path.dirname(__file__) + '/lines.csv')

print(df_pietree)
print(df_lines)

df_curves = []

df_pietree['chart'] = 'pie_tree'
df_curves.append(df_pietree)

df_lines['chart'] = 'lines'
df_curves.append(df_lines)

df_combined = pd.concat(df_curves, axis=0)

df_combined.to_csv(os.path.dirname(__file__) + '/pie_tree_lines.csv', encoding='utf-8', index=False)
print('finished')