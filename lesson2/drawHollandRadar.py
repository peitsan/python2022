#e19.2drawHollandRadar.py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mat
mat.rcParams['font.family'] = 'SimHei'
mat.rcParams['font.sans-serif'] = 'SimHei'
radar_labels = np.array([
  'I','A','S','E','C','R'
])
nAttr = 6
data = np.array([
    [0.40,0.32,0.35,0.30,0.30,0.88],
    [0.85,0.35,0.30,0.40,0.40,0.30],
    [0.43,0.89,0.30,0.28,0.22,0.30],
    [0.30,0.25,0.48,0.85,0.45,0.40],
    [0.20,0.38,0.87,0.45,0.32,0.28],
    [0.34,0.31,0.38,0.40,0.92,0.28]
])

angl = np.linspace(0,2*np.pi,nAttr,endpoint=False)
data = np.concatenate((data,[data[0]]))