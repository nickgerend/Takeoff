# Written by: Nick Gerend, @dataoutsider
# Viz: "Takeoff", enjoy!

import pandas as pd
import numpy as np
import os
from datetime import datetime
from math import pi, cos, sin, sqrt, exp

class point:
    def __init__(self, index, type, level, group, x, y, path, count, node_1='', node_2=''): 
        self.index = index
        self.type = type
        self.level = level
        self.group = group
        self.x = x
        self.y = y
        self.path = path
        self.count = count
        self.node_1 = node_1
        self.node_2 = node_2
    def to_dict(self):
        return {
            'index' : self.index,
            'type' : self.type,
            'level' : self.level,
            'group' : self.group,
            'x' : self.x,
            'y' : self.y,
            'path' : self.path,
            'count' : self.count,
            'node_1' : self.node_1,
            'node_2' : self.node_2}

def sigmoid_xy(x1, y1, x2, y2, points, orientation = 'h', limit = 6):
    x_1 = x1
    y_1 = y1
    x_2 = x2
    y_2 = y2
    if orientation == 'v':
        x1 = y_1
        y1 = x_1
        x2 = y_2
        y2 = x_2
    x = []
    y = []
    amin = 1./(1.+exp(limit))
    amax = 1./(1.+exp(-limit))
    da = amax-amin
    for i in range(points):
        i += 1
        xi = (i-1.)*((2.*limit)/(points-1.))-limit
        yi = ((1.0/(1.0+exp(-xi)))-amin)/da
        x.append((xi-(-limit))/(2.*limit)*(x2-x1)+x1)
        y.append((yi-(0.))/(1.)*(y2-y1)+y1)
    return { 'h': list(zip(x,y)), 'v': list(zip(y,x))}.get(orientation, None)

def rescale(x, xmin, xmax, newmin, newmax):
    rescaled = (newmax-newmin)*((x-xmin)/(xmax-xmin))+newmin
    return rescaled

def DistBtwTwoPnts(x1, y1, x2, y2):
    return sqrt((x2-x1)**2+(y2-y1)**2)

df2020 = pd.read_csv(os.path.dirname(__file__) + '/aircraft_2020.csv', dtype=pd.StringDtype())
groupers = ['index', 'STATE', 'NO-ENG', 'speed_bin']

#region initialize
df_group_count = df2020.groupby(['Registrant'])['index'].count().reset_index(name='r_count')
df2020 = pd.merge(df2020, df_group_count, how='left', left_on=['Registrant'], right_on=['Registrant'])
df_group = df2020.sort_values(['r_count'],ascending=False).groupby(groupers[0:2], sort=False)
vals1 = list(df_group.count().reset_index()['index'].unique())
g1 = np.linspace(0.0, 1.0, num=len(vals1)+1)[1:]
g1 = g1 - (g1[1]-g1[0])/2.
vals2 = list(df2020['STATE'].unique())
g2 = np.linspace(0.0, 1.0, num=len(vals2)+1)[1:]
g2 = g2 - (g2[1]-g2[0])/2.
list_u = []
list_g = []
g_1 = dict(zip(vals1,g1))
g_2 = dict(zip(vals2,g2))
list_u.append(g_1)
list_u.append(g_2)
list_g.append(df_group)
#endregion

#region algorithm

for i in range(len(groupers)-2):
    group_i = groupers[i+1:i+3]
    df_group_i = df2020.groupby(group_i)
    vals = list(df2020[groupers[i+2]].unique())
    gi = np.linspace(0.0, 1.0, num=len(vals)+1)[1:]
    gi = gi - (gi[1]-gi[0])/2.
    g_i = dict(zip(vals,gi))
    list_u.append(g_i)
    list_g.append(df_group_i)
df_group_f = df2020.groupby(groupers[len(groupers)-1])
list_g.append(df_group_f)

ix = 0
list_xy = []
points = 190
for i in range(len(groupers)-1):
    #counts for circles
    count_dict = df2020.groupby(groupers[i+1]).count()['index'].to_dict()
    #draw links
    for keys, items in list_g[i]:
        x1 =list_u[i][keys[0]]
        x2 =list_u[i+1][keys[1]]
        if abs(x2-x1) > 0.5:
            if x2 < 0.5:
                x2 += 1.
            else:
                x2 -= 1.
        y1 = (len(groupers)-i)**2
        y2 = (len(groupers)-i-1)**2
        points_i = int((DistBtwTwoPnts(x1, y1, x2, y2))/8.*points)+10
        count = len(items)
        sigmoid = sigmoid_xy(x1, y1, x2, y2, points_i, orientation = 'v', limit = 9) #10
        group = ','.join(keys)
        for j in range(points_i):
            list_xy.append(point(ix, 'link', i+1, groupers[i]+','+groupers[i+1]+':'+group, sigmoid[j][0], sigmoid[j][1], j, count, keys[0], keys[1]))
            ix += 1
        #collect count nodes
        if i == 0:
            count_L1 = 1
            count_L2 = count_dict[keys[1]]
            list_xy.append(point(ix, 'node', i, groupers[i]+','+groupers[i]+':'+keys[0]+','+ keys[0], x1, y1, 0, count_L1, keys[0], keys[0]))
            list_xy.append(point(ix, 'node', i+1, groupers[i]+','+groupers[i+1]+':'+group, x2, y2, 0, count_L2, keys[0], keys[1]))
        else:
            count_L = count_dict[keys[1]]
            list_xy.append(point(ix, 'node', i+1, groupers[i]+','+groupers[i+1]+':'+group, x2, y2, 0, count_L, keys[0], keys[1]))
#endregion

df_out = pd.DataFrame.from_records([s.to_dict() for s in list_xy])
#df_out.to_csv(os.path.dirname(__file__) + '/lines.csv', encoding='utf-8', index=False)

#region curved output
ix = 0
N = 1.0
offset = 1.0
min_x = 0
c_points = 10
c_factor = len(df2020)
import csv
with open(os.path.dirname(__file__) + '/lines.csv', 'w',) as csvfile:
    writer = csv.writer(csvfile, lineterminator = '\n')
    writer.writerow(['index', 'type', 'level', 'group', 'x', 'y', 'path', 'count', 'node1', 'node2'])
    for i in range(len(list_xy)):       

        type = list_xy[i].type
        level = list_xy[i].level
        group = list_xy[i].group
        path = list_xy[i].path
        count = list_xy[i].count
        node1 = list_xy[i].node_1
        node2 = list_xy[i].node_2

        t = list_xy[i].x
        v = list_xy[i].y
        angle = (2.*pi)*(((t-min_x)%(N))/(N))
        angle_deg = angle * 180./pi
        angle_rotated = (abs(angle_deg-360.)+90.) % 360. 
        angle_new = angle_rotated * pi/180.

        o = offset
        x_out = (o+v)*cos(angle_new)
        y_out = (o+v)*sin(angle_new)
        x_out = rescale(x_out, -16-offset, 16+offset, -1.5, 1.5)
        y_out = rescale(y_out, -16-offset, 16+offset, -1.5, 1.5)

        writer.writerow([ix, type, level, group, x_out, y_out, path, count, node1, node2])
        ix += 1
#endregion

print('finished')