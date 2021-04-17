# Written by: Nick Gerend, @dataoutsider
# Viz: "", enjoy!

import pandas as pd
import numpy as np
import os
from datetime import datetime
from math import pi, cos, sin, sqrt, exp

def circle(diam, points):
    x = []
    y = []
    path = []
    angle = 0.
    path_i = 1
    for i in range(points):
        x.append(diam/2.*sin(angle*pi/180.))
        y.append(diam/2.*cos(angle*pi/180.))
        path.append(path_i)
        angle += 1./(points-1)*360.
        path_i += 1
    return x,y,path

count = 500
circ = circle(4.4, count)
import csv
with open(os.path.dirname(__file__) + '/background.csv', 'w',) as csvfile:
    writer = csv.writer(csvfile, lineterminator = '\n')
    writer.writerow(['index', 'x', 'y', 'path'])
    for i in range(count):       
        writer.writerow([i, circ[0][i], circ[1][i], circ[2][i]])
    writer.writerow([i, 0, 2.5, count+1])
    writer.writerow([i, 2.5, 2.5, count+2])
    writer.writerow([i, 2.5, -2.5, count+3])
    writer.writerow([i, -2.5, -2.5, count+4])
    writer.writerow([i, -2.5, 2.5, count+5])
    writer.writerow([i, 0, 2.5, count+6])

print('finished')