# Written by: Nick Gerend, @dataoutsider
# Viz: "Takeoff", enjoy!

import pandas as pd
import numpy as np
import os
from datetime import datetime
from math import pi, cos, sin, sqrt, exp

width = 0.25
ht = 3.
lh = 2.
import csv
with open(os.path.dirname(__file__) + '/T.csv', 'w',) as csvfile:
    writer = csv.writer(csvfile, lineterminator = '\n')
    writer.writerow(['x', 'y', 'path'])

    writer.writerow([-lh/2., 0., 1])
    writer.writerow([lh/2., 0., 2])
    writer.writerow([lh/2, -width, 3])
    writer.writerow([width/2., -width, 4])
    writer.writerow([width/2., -ht, 5])
    writer.writerow([-width/2., -ht, 6])
    writer.writerow([-width/2., -width, 7])
    writer.writerow([-lh/2, -width, 8])
    writer.writerow([-lh/2, 0.0, 9])

print('finished')