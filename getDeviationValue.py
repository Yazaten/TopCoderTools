# -*- coding: utf-8 -*-
import numpy as np
import sys

score = 1500

CPList = []
for line in sys.stdin:
	CPList.append(int(line))

sig = np.std(CPList)
ave = np.average(CPList)

print (int)(np.round_(50+10*(score-ave)/sig))
